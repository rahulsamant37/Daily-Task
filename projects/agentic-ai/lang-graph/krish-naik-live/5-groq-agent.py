from langgraph.graph.message import add_messages
from langgraph.graph import MessageGraph, StateGraph, START, END
from langgraph.graph import MessagesState
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import ToolNode
from langchain_core.tools import tool
from langchain_core.runnables import Runnable
from langchain_core.messages import HumanMessage, SystemMessage, BaseMessage
from langchain_groq import ChatGroq

from pprint import pprint
from typing import Annotated
from typing_extensions import TypedDict
from IPython.display import display, Image
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
os.environ["LANGSMITH_API_KEY"]=os.getenv("LANGSMITH_API_KEY")
llm=ChatGroq(model="qwen-2.5-32b")

## Defining the model
def llm_calling(state):
    """
    Calling my LLM model
    """
    return {'messages':[llm.invoke(MessagesState['messages'])]}

def make_default_graph():
    """
    Make a simple LLM agent
    """
    workflow=StateGraph(MessagesState)

    ## addding node
    workflow.add_node("llm",llm_calling)

    ## adding edges
    workflow.add_edge(START,"llm")
    workflow.add_edge("llm",END)

    ## compile the workflow
    graph=workflow.compile()
    return graph

def make_alternative_graph():
    """
    Make a tool-calling agent
    """

    ## Defining tools
    @tool
    def add(x:int,y:int):
        """Add two numbers"""
        return x+y
    
    ## Binding the tools to the model
    tools=[add]
    tool_node=ToolNode(tools)
    model_with_tools = llm.bind_tools(tools)

    ## Defining the tools node
    def call_model_with_tools(state):
        return {'messages':[model_with_tools.invoke(MessagesState['messages'])]}
    
    ## Defining conditional edge
    def should_continue(state:MessagesState):
        if state['messages'][-1].tool_calls:
            return "tools"
        else:
            return END

    workflow=StateGraph(MessagesState)

    ## addding node
    workflow.add_node("llm",call_model_with_tools)
    workflow.add_node("tools",tool_node)

    ## adding edges
    workflow.add_edge(START,"llm")
    workflow.add_edge("llm","tools")
    workflow.add_conditional_edges("tools",should_continue)

    ## compile the workflow
    graph=workflow.compile()
    return graph

agent=make_alternative_graph()