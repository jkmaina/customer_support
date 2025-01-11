from langchain.prompts import ChatPromptTemplate
import operator
from typing import Annotated, Sequence, TypedDict
from langchain_openai import ChatOpenAI
from langchain.schema import BaseMessage, AIMessage
from langgraph.graph import StateGraph, START, END
from enum import Enum

class IntentEnum(str, Enum):
    CHECK_ORDER = "check_order"
    PRODUCT_INQUIRY = "product_inquiry"
    ESCALATE = "escalate"
    UNKNOWN = "unknown"
    GENERAL_CHAT = "general_chat"

class CustomerState(TypedDict):
    """State for customer support workflow"""
    messages: Annotated[Sequence[BaseMessage], operator.add]
    intent: str
    status: str

# Prompts
intent_prompt = ChatPromptTemplate.from_messages([
    ("system", """You are a customer support intent classifier.
    Classify the user query into one of these intents: check_order, product_inquiry,
    escalate, general_chat, or unknown. Respond with just the intent."""),
    ("human", "{query}")
])

order_prompt = ChatPromptTemplate.from_messages([
    ("system", """You are a customer service agent checking order status.
    Available orders: #12345 (shipped), #67890 (processing).
    If the order number is not found, apologize and provide support options."""),
    ("human", "{query}")
])

product_prompt = ChatPromptTemplate.from_messages([
    ("system", """You are a product information specialist.
    Products: wireless headphones (20-hour battery, noise cancellation),
    smartwatch (fitness tracking, heart rate monitoring).
    For unknown products, apologize and offer to connect with a specialist."""),
    ("human", "{query}")
])

general_chat_prompt = ChatPromptTemplate.from_messages([
    ("system", """You are a helpful customer service assistant. 
    Always greet users by name if they provide it, and ask how you can assist them today.
    Be friendly and professional in your responses."""),
    ("human", "{query}")
])

def intent_classifier_node(state: CustomerState):
    """Classify customer intent using LLM"""
    llm = ChatOpenAI(model="gpt-4o-mini")
    classifier_chain = intent_prompt | llm
    query = state["messages"][-1].content
    # Ensure we only get one intent by taking the first one if multiple are returned
    intent = classifier_chain.invoke({"query": query}).content.strip().lower().split()[0]
    # Validate the intent is one of our enum values
    try:
        validated_intent = IntentEnum(intent)
        state["intent"] = validated_intent
    except ValueError:
        # Default to unknown if intent isn't recognized
        state["intent"] = IntentEnum.UNKNOWN
    return state

def order_status_node(state: CustomerState):
    """Handle order status queries using LLM"""
    llm = ChatOpenAI(model="gpt-4o-mini")
    order_chain = order_prompt | llm
    query = state["messages"][-1].content
    response = order_chain.invoke({"query": query})
    state["messages"].append(AIMessage(content=response.content))
    return state

def product_inquiry_node(state: CustomerState):
    """Handle product inquiries using LLM"""
    llm = ChatOpenAI(model="gpt-4o-mini")
    product_chain = product_prompt | llm
    query = state["messages"][-1].content
    response = product_chain.invoke({"query": query})
    state["messages"].append(AIMessage(content=response.content))
    return state

def general_chat_node(state: CustomerState):
    """Handle general conversation and queries"""
    llm = ChatOpenAI(model="gpt-4o-mini")
    chat_chain = general_chat_prompt | llm
    query = state["messages"][-1].content
    response = chat_chain.invoke({"query": query})
    state["messages"].append(AIMessage(content=response.content))
    return state

def build_support_workflow():
    """Build the complete customer support workflow"""
    workflow = StateGraph(CustomerState)
    
    # Add nodes
    workflow.add_node("intent_classifier", intent_classifier_node)
    workflow.add_node("order_status", order_status_node)
    workflow.add_node("product_inquiry", product_inquiry_node)
    workflow.add_node("general_chat", general_chat_node)
    
    # Add conditional routing
    workflow.add_edge(START, "intent_classifier")
    
    # Route based on intent
    workflow.add_conditional_edges(
        "intent_classifier",
        lambda x: x["intent"],
        {
            IntentEnum.CHECK_ORDER: "order_status",
            IntentEnum.PRODUCT_INQUIRY: "product_inquiry",
            IntentEnum.GENERAL_CHAT: "general_chat",
            IntentEnum.UNKNOWN: "general_chat",  # Default to general chat for unknown intents
            IntentEnum.ESCALATE: "general_chat"  # Handle escalation in general chat for now
        }
    )
    
    # Add edges to END
    workflow.add_edge("order_status", END)
    workflow.add_edge("product_inquiry", END)
    workflow.add_edge("general_chat", END)
    
    return workflow.compile()