import json
from typing import List, Tuple, Dict, Any

from deepeval import evaluate
from deepeval.metrics import GEval, FaithfulnessMetric, ContextualRelevancyMetric
from deepeval.test_case import LLMTestCase, LLMTestCaseParams
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from helper_functions import (
    create_question_answer_from_context_chain,
    answer_question_from_context,
    retrieve_context_per_question
)


def get_llm(provider: str = "gemini", model: str = None):
    """
    Get a free LLM instance based on the provider.
    
    Args:
        provider: The LLM provider ("gemini", "ollama", "groq")
        model: Specific model name (optional)
    
    Returns:
        LLM instance
    """
    if provider == "gemini":
        from langchain_google_genai import ChatGoogleGenerativeAI
        return ChatGoogleGenerativeAI(
            model=model or "gemini-2.0-flash",
            temperature=0,
        )
    elif provider == "ollama":
        try:
            from langchain_ollama import ChatOllama
            return ChatOllama(
                model=model or "llama3.2",
                temperature=0
            )
        except ImportError:
            raise ImportError("Please install langchain-ollama: pip install langchain-ollama")
    elif provider == "groq":
        try:
            from langchain_groq import ChatGroq
            return ChatGroq(
                model=model or "llama-3.1-70b-versatile",
                temperature=0
            )
        except ImportError:
            raise ImportError("Please install langchain-groq: pip install langchain-groq")
    else:
        raise ValueError(f"Unsupported provider: {provider}. Use 'gemini', 'ollama', or 'groq'")


def get_default_llm():
    """
    Returns the default free LLM (Google Gemini).
    
    Returns:
        ChatGoogleGenerativeAI: A Google Gemini LLM instance.
    """
    return ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        temperature=0,
    )

def create_deep_eval_test_cases(
    questions: List[str],
    gt_answers: List[str],
    generated_answers: List[str],
    retrieved_documents: List[str]
) -> List[LLMTestCase]:
    """
    Create a list of LLMTestCase objects for evaluation.

    Args:
        questions (List[str]): List of input questions.
        gt_answers (List[str]): List of ground truth answers.
        generated_answers (List[str]): List of generated answers.
        retrieved_documents (List[str]): List of retrieved documents.

    Returns:
        List[LLMTestCase]: List of LLMTestCase objects.
    """
    return [
        LLMTestCase(
            input=question,
            expected_output=gt_answer,
            actual_output=generated_answer,
            retrieval_context=retrieved_document
        )
        for question, gt_answer, generated_answer, retrieved_document in zip(
            questions, gt_answers, generated_answers, retrieved_documents
        )
    ]

# Custom evaluation functions using free models (no deepeval dependency)
def evaluate_relevance(question: str, context: str, llm) -> float:
    """
    Evaluate how relevant the retrieved context is to the question using free LLM.
    
    Args:
        question: The input question
        context: Retrieved context
        llm: Free LLM instance
    
    Returns:
        Relevance score between 0-1
    """
    prompt = PromptTemplate.from_template("""
    Question: {question}
    Context: {context}
    
    Rate how relevant the context is to answering the question on a scale of 0 to 1 (where 1 is perfectly relevant).
    Consider:
    - Does the context contain information needed to answer the question?
    - Is the information directly related to the question?
    
    Respond with only a number between 0 and 1:
    """)
    
    chain = prompt | llm | StrOutputParser()
    try:
        result = chain.invoke({"question": question, "context": context})
        score = float(result.strip())
        return max(0, min(1, score))  # Ensure score is between 0 and 1
    except:
        return 0.5  # Default score if parsing fails

def evaluate_faithfulness(answer: str, context: str, llm) -> float:
    """
    Evaluate if the answer is faithful to the provided context using free LLM.
    
    Args:
        answer: Generated answer
        context: Source context
        llm: Free LLM instance
    
    Returns:
        Faithfulness score between 0-1
    """
    prompt = PromptTemplate.from_template("""
    Answer: {answer}
    Context: {context}
    
    Rate how faithful the answer is to the context on a scale of 0 to 1 (where 1 is completely faithful).
    Consider:
    - Does the answer only use information from the context?
    - Are there any hallucinations or made-up facts?
    
    Respond with only a number between 0 and 1:
    """)
    
    chain = prompt | llm | StrOutputParser()
    try:
        result = chain.invoke({"answer": answer, "context": context})
        score = float(result.strip())
        return max(0, min(1, score))  # Ensure score is between 0 and 1
    except:
        return 0.5  # Default score if parsing fails

def evaluate_correctness(expected: str, actual: str, llm) -> float:
    """
    Evaluate how correct the actual answer is compared to expected using free LLM.
    
    Args:
        expected: Expected/ground truth answer
        actual: Generated answer
        llm: Free LLM instance
    
    Returns:
        Correctness score between 0-1
    """
    prompt = PromptTemplate.from_template("""
    Expected Answer: {expected}
    Actual Answer: {actual}
    
    Rate how correct the actual answer is compared to the expected answer on a scale of 0 to 1 (where 1 is perfectly correct).
    Consider:
    - Factual accuracy
    - Completeness of information
    - Semantic similarity
    
    Respond with only a number between 0 and 1:
    """)
    
    chain = prompt | llm | StrOutputParser()
    try:
        result = chain.invoke({"expected": expected, "actual": actual})
        score = float(result.strip())
        return max(0, min(1, score))  # Ensure score is between 0 and 1
    except:
        return 0.5  # Default score if parsing fails

def evaluate_rag(retriever, num_questions: int = 5, llm_provider: str = "gemini") -> Dict[str, Any]:
    """
    Evaluates a RAG system using free models and custom evaluation functions.
    
    Args:
        retriever: The retriever component to evaluate
        num_questions: Number of test questions to generate
        llm_provider: LLM provider to use ("gemini", "ollama", "groq")
    
    Returns:
        Dict containing evaluation metrics
    """
    
    # Initialize LLM with free alternative
    llm = get_llm(llm_provider)
    
    # Generate test questions about climate change
    question_gen_prompt = PromptTemplate.from_template("""
    Generate {num_questions} diverse questions about climate change that can be answered using scientific information.
    
    Format: Return each question on a new line, numbered 1., 2., etc.
    
    Example questions:
    1. What are the main causes of climate change?
    2. How do greenhouse gases affect global temperature?
    
    Generate {num_questions} questions:
    """)
    
    question_chain = question_gen_prompt | llm | StrOutputParser()
    
    try:
        questions_text = question_chain.invoke({"num_questions": num_questions})
        # Parse questions from numbered list
        questions = []
        for line in questions_text.split('\n'):
            line = line.strip()
            if line and any(line.startswith(f"{i}.") for i in range(1, num_questions + 1)):
                # Remove the number and clean the question
                question = line.split('.', 1)[1].strip()
                if question:
                    questions.append(question)
        
        # Limit to requested number
        questions = questions[:num_questions]
        
    except Exception as e:
        print(f"Error generating questions: {e}")
        # Fallback questions
        questions = [
            "What are the main causes of climate change?",
            "How do greenhouse gases affect global temperature?",
            "What are the impacts of climate change on ecosystems?",
            "What are renewable energy solutions for climate change?",
            "How does deforestation contribute to climate change?"
        ][:num_questions]
    
    # Evaluate each question
    results = []
    total_relevance = 0
    total_questions = len(questions)
    
    for i, question in enumerate(questions):
        try:
            # Get retrieval results
            context_docs = retriever.get_relevant_documents(question)
            context_text = "\n".join([doc.page_content for doc in context_docs])
            
            # Evaluate relevance
            relevance_score = evaluate_relevance(question, context_text, llm)
            total_relevance += relevance_score
            
            result = {
                "question": question,
                "context_length": len(context_text),
                "num_docs_retrieved": len(context_docs),
                "relevance_score": relevance_score
            }
            
            results.append(result)
            print(f"Question {i+1}/{total_questions}: Relevance = {relevance_score:.2f}")
            
        except Exception as e:
            print(f"Error evaluating question {i+1}: {e}")
            results.append({
                "question": question,
                "error": str(e),
                "relevance_score": 0.0
            })
    
    # Calculate averages
    avg_relevance = total_relevance / total_questions if total_questions > 0 else 0
    
    return {
        "questions": questions,
        "individual_results": results,
        "summary": {
            "total_questions": total_questions,
            "average_relevance": avg_relevance,
            "model_used": llm_provider,
            "evaluation_method": "free_custom_functions"
        }
    }


def evaluate_test_cases(
    questions: List[str],
    expected_answers: List[str],
    generated_answers: List[str],
    contexts: List[str],
    llm_provider: str = "gemini"
) -> Dict[str, Any]:
    """
    Evaluate RAG system using provided test cases with free models.
    
    Args:
        questions: List of test questions
        expected_answers: List of expected answers
        generated_answers: List of generated answers  
        contexts: List of retrieved contexts
        llm_provider: LLM provider to use
    
    Returns:
        Comprehensive evaluation results
    """
    llm = get_llm(llm_provider)
    
    results = []
    total_correctness = 0
    total_faithfulness = 0
    total_relevance = 0
    
    for i, (question, expected, generated, context) in enumerate(zip(
        questions, expected_answers, generated_answers, contexts
    )):
        try:
            # Evaluate different aspects
            correctness = evaluate_correctness(expected, generated, llm)
            faithfulness = evaluate_faithfulness(generated, context, llm)
            relevance = evaluate_relevance(question, context, llm)
            
            total_correctness += correctness
            total_faithfulness += faithfulness
            total_relevance += relevance
            
            result = {
                "question": question,
                "expected_answer": expected,
                "generated_answer": generated,
                "context": context[:200] + "..." if len(context) > 200 else context,
                "scores": {
                    "correctness": correctness,
                    "faithfulness": faithfulness,
                    "relevance": relevance
                }
            }
            results.append(result)
            print(f"Test case {i+1}: Correctness={correctness:.2f}, Faithfulness={faithfulness:.2f}, Relevance={relevance:.2f}")
            
        except Exception as e:
            print(f"Error evaluating test case {i+1}: {e}")
            results.append({
                "question": question,
                "error": str(e),
                "scores": {"correctness": 0.0, "faithfulness": 0.0, "relevance": 0.0}
            })
    
    num_cases = len(questions)
    return {
        "individual_results": results,
        "summary": {
            "total_cases": num_cases,
            "average_scores": {
                "correctness": total_correctness / num_cases if num_cases > 0 else 0,
                "faithfulness": total_faithfulness / num_cases if num_cases > 0 else 0,
                "relevance": total_relevance / num_cases if num_cases > 0 else 0
            },
            "model_used": llm_provider,
            "evaluation_method": "free_custom_functions"
        }
    }


def simple_rag_evaluation(retriever, test_question: str = None, llm_provider: str = "gemini") -> Dict[str, Any]:
    """
    Simple RAG evaluation for quick testing.
    
    Args:
        retriever: The retriever component
        test_question: Optional test question (uses default if not provided)
        llm_provider: LLM provider to use
    
    Returns:
        Simple evaluation results
    """
    if test_question is None:
        test_question = "What are the main causes of climate change?"
    
    llm = get_llm(llm_provider)
    
    try:
        # Get retrieval results
        context_docs = retriever.invoke(test_question)
        context_text = "\n".join([doc.page_content for doc in context_docs])
        
        # Evaluate relevance
        relevance_score = evaluate_relevance(test_question, context_text, llm)
        
        return {
            "question": test_question,
            "num_docs_retrieved": len(context_docs),
            "context_length": len(context_text),
            "relevance_score": relevance_score,
            "context_preview": context_text[:300] + "..." if len(context_text) > 300 else context_text,
            "model_used": llm_provider,
            "evaluation_method": "simple_free_evaluation"
        }
        
    except Exception as e:
        return {
            "question": test_question,
            "error": str(e),
            "model_used": llm_provider
        }


def calculate_average_scores(results: List[Dict]) -> Dict[str, float]:
    """
    Calculate average scores across all evaluation results.
    
    Args:
        results: List of evaluation result dictionaries
    
    Returns:
        Dictionary with average scores for each metric
    """
    if not results:
        return {}
    
    # Initialize score accumulators
    score_sums = {}
    score_counts = {}
    
    for result in results:
        if isinstance(result, str):
            try:
                # Try to parse JSON result
                result_dict = json.loads(result)
                for metric, score in result_dict.items():
                    if isinstance(score, (int, float)):
                        score_sums[metric] = score_sums.get(metric, 0) + score
                        score_counts[metric] = score_counts.get(metric, 0) + 1
            except (json.JSONDecodeError, TypeError):
                continue
        elif isinstance(result, dict):
            for metric, score in result.items():
                if isinstance(score, (int, float)):
                    score_sums[metric] = score_sums.get(metric, 0) + score
                    score_counts[metric] = score_counts.get(metric, 0) + 1
    
    # Calculate averages
    averages = {}
    for metric in score_sums:
        if score_counts[metric] > 0:
            averages[metric] = score_sums[metric] / score_counts[metric]
    
    return averages


def run_comprehensive_evaluation(
    retriever,
    test_cases: List[LLMTestCase],
    llm_provider: str = "gemini"
) -> Dict[str, Any]:
    """
    Run comprehensive evaluation using deepeval metrics.
    
    Args:
        retriever: The retriever component
        test_cases: List of LLMTestCase objects
        llm_provider: LLM provider to use
    
    Returns:
        Comprehensive evaluation results
    """
    
    # Use free model for evaluation metrics
    model_name = "gemini-2.0-flash" if llm_provider == "gemini" else "llama3.2"
    
    # Update metrics to use free models
    metrics = [
        GEval(
            name="Correctness",
            model=model_name,
            evaluation_params=[
                LLMTestCaseParams.EXPECTED_OUTPUT,
                LLMTestCaseParams.ACTUAL_OUTPUT
            ],
            evaluation_steps=[
                "Determine whether the actual output is factually correct based on the expected output."
            ],
        ),
        FaithfulnessMetric(
            threshold=0.7,
            model=model_name,
            include_reason=False
        ),
        ContextualRelevancyMetric(
            threshold=1,
            model=model_name,
            include_reason=True
        )
    ]
    
    # Run evaluation
    results = evaluate(test_cases, metrics)
    
    return {
        "individual_results": results,
        "summary": {
            "total_cases": len(test_cases),
            "metrics_used": [metric.name for metric in metrics],
            "model_used": model_name
        }
    }

if __name__ == "__main__":
    """
    Example usage of the updated RAG evaluation script.
    
    This demonstrates how to use free models for RAG evaluation.
    """
    
    # Example: Set up your retriever and run evaluation
    print("RAG Evaluation Script with Free Models")
    print("=====================================")
    print("Supported free models:")
    print("- Google Gemini (gemini-2.0-flash) - Default")
    print("- Ollama (local models)")
    print("- Groq (fast free inference)")
    print()
    
    # Example configuration
    example_questions = [
        "What is climate change?",
        "How do greenhouse gases affect the environment?",
        "What are renewable energy sources?"
    ]
    
    example_gt_answers = [
        "Climate change refers to long-term shifts in global temperatures and weather patterns.",
        "Greenhouse gases trap heat in Earth's atmosphere, causing global warming.",
        "Renewable energy sources include solar, wind, hydro, and geothermal power."
    ]
    
    example_generated_answers = [
        "Climate change is the long-term alteration of temperature and weather patterns globally.",
        "Greenhouse gases create a warming effect by trapping solar radiation.",
        "Solar, wind, hydroelectric, and geothermal are examples of renewable energy."
    ]
    
    example_contexts = [
        "Climate change context document...",
        "Greenhouse gas effects document...",
        "Renewable energy sources document..."
    ]
    
    # Create test cases
    test_cases = create_deep_eval_test_cases(
        example_questions,
        example_gt_answers,
        example_generated_answers,
        example_contexts
    )
    
    print(f"Created {len(test_cases)} test cases for evaluation")
    print("To run evaluation, uncomment the following lines and provide your retriever:")
    print("# results = run_comprehensive_evaluation(your_retriever, test_cases)")
    print("# print('Evaluation Results:', results)")
    
    # Uncomment and modify the following lines to run actual evaluation:
    # if 'your_retriever' in locals():
    #     results = evaluate_rag(your_retriever, num_questions=3, llm_provider="gemini")
    #     print("Quick evaluation results:", results)
