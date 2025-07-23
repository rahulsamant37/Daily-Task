# RAG Techniques Collection

A comprehensive collection of **Retrieval-Augmented Generation (RAG)** techniques implemented in Jupyter notebooks. This repository demonstrates various advanced RAG methodologies, from basic implementations to cutting-edge approaches that enhance information retrieval and generation capabilities.

## 🎯 Overview

This collection contains 35+ RAG technique implementations, each designed to solve specific challenges in document retrieval, query processing, and answer generation. All notebooks are executable and include detailed explanations, code implementations, and practical examples.

## 📚 Available Techniques

### Basic RAG Implementations
- **[Simple RAG](all_rag_techniques/simple_rag.ipynb)** - Basic RAG system with PDF processing and FAISS vector store
- **[Simple CSV RAG](all_rag_techniques/simple_csv_rag.ipynb)** - RAG implementation for CSV data sources
- **[Simple RAG with LlamaIndex](all_rag_techniques/simple_rag_with_llamaindex.ipynb)** - LlamaIndex framework implementation
- **[Simple CSV RAG with LlamaIndex](all_rag_techniques/simple_csv_rag_with_llamaindex.ipynb)** - CSV processing with LlamaIndex

### Advanced Retrieval Techniques
- **[HyDE (Hypothetical Document Embedding)](all_rag_techniques/HyDe_Hypothetical_Document_Embedding.ipynb)** - Transforms queries into hypothetical documents for better matching
- **[HyPE (Hypothetical Prompt Embeddings)](all_rag_techniques/HyPE_Hypothetical_Prompt_Embeddings.ipynb)** - Enhanced prompt embedding techniques
- **[Query Transformations](all_rag_techniques/query_transformations.ipynb)** - Multiple query transformation strategies
- **[Fusion Retrieval](all_rag_techniques/fusion_retrieval.ipynb)** - Combines multiple retrieval approaches
- **[Fusion Retrieval with LlamaIndex](all_rag_techniques/fusion_retrieval_with_llamaindex.ipynb)** - LlamaIndex implementation of fusion retrieval
- **[Adaptive Retrieval](all_rag_techniques/adaptive_retrieval.ipynb)** - Dynamic retrieval adaptation based on query complexity

### Self-Improving RAG Systems
- **[Self-RAG](all_rag_techniques/self_rag.ipynb)** - Self-reflective RAG with dynamic retrieval decisions
- **[Reliable RAG](all_rag_techniques/reliable_rag.ipynb)** - Enhanced reliability and consistency in RAG responses
- **[Retrieval with Feedback Loop](all_rag_techniques/retrieval_with_feedback_loop.ipynb)** - Iterative improvement through feedback mechanisms

### Graph-Based RAG
- **[GraphRAG](all_rag_techniques/graph_rag.ipynb)** - Graph-enhanced RAG with knowledge graph integration
- **[Microsoft GraphRAG](all_rag_techniques/Microsoft_GraphRag.ipynb)** - Microsoft's approach to graph-based RAG
- **[GraphRAG with Milvus VectorDB](all_rag_techniques/001_graphrag_with_milvus_vectordb.ipynb)** - GraphRAG implementation using Milvus vector database

### Corrective and Adaptive RAG
- **[CRAG (Corrective RAG)](all_rag_techniques/crag.ipynb)** - Self-correcting RAG system with validation mechanisms
- **[RAPTOR](all_rag_techniques/raptor.ipynb)** - Recursive abstractive processing for tree-organized retrieval

### Chunking and Context Enhancement
- **[Semantic Chunking](all_rag_techniques/semantic_chunking.ipynb)** - Intelligent text segmentation based on semantic boundaries
- **[Contextual Chunking](all_rag_techniques/contextual_chunk_headers.ipynb)** - Enhanced chunking with contextual headers
- **[Proposition Chunking](all_rag_techniques/proposition_chunking.ipynb)** - Proposition-based text segmentation
- **[Choose Chunk Size](all_rag_techniques/choose_chunk_size.ipynb)** - Optimal chunk size selection strategies
- **[Context Enrichment Window](all_rag_techniques/context_enrichment_window_around_chunk.ipynb)** - Window-based context enhancement
- **[Context Enrichment with LlamaIndex](all_rag_techniques/context_enrichment_window_around_chunk_with_llamaindex.ipynb)** - LlamaIndex implementation of context enrichment

### Reranking and Filtering
- **[Reranking](all_rag_techniques/reranking.ipynb)** - Document reranking for improved relevance
- **[Reranking with LlamaIndex](all_rag_techniques/reranking_with_llamaindex.ipynb)** - LlamaIndex-based reranking implementation
- **[Contextual Compression](all_rag_techniques/contextual_compression.ipynb)** - Intelligent context compression techniques
- **[Relevant Segment Extraction](all_rag_techniques/relevant_segment_extraction.ipynb)** - Extracting most relevant document segments

### Multimodal RAG
- **[Multi-Modal RAG with Captioning](all_rag_techniques/multi_model_rag_with_captioning.ipynb)** - RAG with image captioning capabilities
- **[Multi-Modal RAG with ColPali](all_rag_techniques/multi_model_rag_with_colpali.ipynb)** - Advanced multimodal RAG using ColPali

### Hierarchical and Structured RAG
- **[Hierarchical Indices](all_rag_techniques/hierarchical_indices.ipynb)** - Multi-level indexing for better organization
- **[Document Augmentation](all_rag_techniques/document_augmentation.ipynb)** - Enhanced document preprocessing and augmentation

### Specialized Techniques
- **[Explainable Retrieval](all_rag_techniques/explainable_retrieval.ipynb)** - Transparent and interpretable retrieval processes
- **[Dartboard](all_rag_techniques/dartboard.ipynb)** - Precision-focused retrieval technique

## 🚀 Getting Started

### Prerequisites
```bash
pip install -r requirements.txt
```

### Required Libraries
- `langchain`
- `faiss-cpu`
- `openai`
- `transformers`
- `sentence-transformers`
- `llama-index`
- `milvus-lite`
- `pypdf`
- `chromadb`

### Basic Usage
1. Choose a technique from the collection
2. Open the corresponding Jupyter notebook
3. Follow the step-by-step implementation
4. Customize parameters for your specific use case

## 📁 Directory Structure
```
RAG_Techniques/
├── all_rag_techniques/           # Main collection of RAG techniques
│   ├── simple_rag.ipynb
│   ├── graph_rag.ipynb
│   ├── self_rag.ipynb
│   └── ... (35+ notebooks)
├── all_rag_techniques_runnable_scripts/  # (Future: Python scripts)
└── README.md                     # This file
```

## 🔧 Key Features

- **Comprehensive Coverage**: 35+ different RAG techniques
- **Practical Examples**: Each notebook includes working code examples
- **Multiple Frameworks**: Implementations using LangChain, LlamaIndex, and custom solutions
- **Vector Database Support**: Integration with FAISS, Milvus, ChromaDB
- **Multimodal Capabilities**: Text, image, and document processing
- **Evaluation Metrics**: Built-in evaluation functions for technique comparison

## 📊 Technique Categories

| Category | Count | Examples |
|----------|-------|----------|
| Basic RAG | 4 | Simple RAG, CSV RAG |
| Advanced Retrieval | 6 | HyDE, Fusion Retrieval, Query Transformations |
| Self-Improving | 3 | Self-RAG, Reliable RAG, Feedback Loop |
| Graph-Based | 3 | GraphRAG, Microsoft GraphRAG |
| Chunking & Context | 6 | Semantic Chunking, Context Enrichment |
| Reranking | 4 | Document Reranking, Contextual Compression |
| Multimodal | 2 | Captioning RAG, ColPali RAG |
| Specialized | 7+ | Explainable Retrieval, Hierarchical Indices |

## 🎓 Learning Path

### Beginner
1. Start with [Simple RAG](all_rag_techniques/simple_rag.ipynb)
2. Explore [Semantic Chunking](all_rag_techniques/semantic_chunking.ipynb)
3. Try [Reranking](all_rag_techniques/reranking.ipynb)

### Intermediate
1. Implement [HyDE](all_rag_techniques/HyDe_Hypothetical_Document_Embedding.ipynb)
2. Experiment with [Fusion Retrieval](all_rag_techniques/fusion_retrieval.ipynb)
3. Build [Self-RAG](all_rag_techniques/self_rag.ipynb)

### Advanced
1. Deploy [GraphRAG](all_rag_techniques/graph_rag.ipynb)
2. Implement [RAPTOR](all_rag_techniques/raptor.ipynb)
3. Create [Multimodal RAG](all_rag_techniques/multi_model_rag_with_captioning.ipynb)

## 🔗 External Resources

- **Google Colab**: All notebooks include Colab badges for easy cloud execution
- **Original Repository**: Based on [NirDiamant/RAG_Techniques](https://github.com/NirDiamant/RAG_Techniques)
- **Documentation**: Each notebook contains detailed explanations and method descriptions

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Add new RAG techniques or improve existing ones
4. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 🏷️ Tags

`RAG` `Retrieval-Augmented-Generation` `NLP` `LangChain` `LlamaIndex` `Vector-Database` `Machine-Learning` `AI` `Information-Retrieval` `Document-Processing`

---

**Last Updated**: July 2025  
**Total Techniques**: 35+  
**Status**: Active Development