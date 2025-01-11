from src.support_agent import (
    build_support_workflow,
    general_chat_node,
    intent_classifier_node,
    order_status_node,
    product_inquiry_node,
    IntentEnum
)
from langchain.schema import HumanMessage

def test_intent_classifier():
    """Test the intent classifier node"""
    state = {
        "messages": [HumanMessage(content="Where is my order #12345?")],
        "intent": "",
        "status": ""
    }
    result = intent_classifier_node(state)
    assert result["intent"] == IntentEnum.CHECK_ORDER

def test_order_status():
    """Test the order status node"""
    state = {
        "messages": [HumanMessage(content="Where is my order #12345?")],
        "intent": IntentEnum.CHECK_ORDER,
        "status": ""
    }
    result = order_status_node(state)
    response_text = result["messages"][-1].content.lower()
    assert "shipped" in response_text or "processing" in response_text

def test_product_inquiry():
    """Test the product inquiry node"""
    state = {
        "messages": [HumanMessage(content="Tell me about wireless headphones")],
        "intent": IntentEnum.PRODUCT_INQUIRY,
        "status": ""
    }
    result = product_inquiry_node(state)
    response_text = result["messages"][-1].content.lower()
    assert "wireless headphones" in response_text

def test_general_chat():
    """Test general conversation handling"""
    state = {
        "messages": [HumanMessage(content="Hello, I'm James")],
        "intent": IntentEnum.GENERAL_CHAT,
        "status": ""
    }
    result = general_chat_node(state)
    response_text = result["messages"][-1].content.lower()
    assert "how can i assist you today?" in response_text and "james" in response_text

def test_complete_workflow():
    """Test the complete customer support workflow"""
    workflow = build_support_workflow()
    
    # Test order status
    state = {"messages": [HumanMessage(content="Where is my order #12345?")],
            "intent": "",
            "status": ""}
    result = workflow.invoke(state)
    assert "shipped" in result["messages"][-1].content.lower()
    
    # Test product inquiry
    state = {"messages": [HumanMessage(content="Tell me about wireless headphones")],
            "intent": "",
            "status": ""}
    result = workflow.invoke(state)
    assert "wireless headphones" in result["messages"][-1].content.lower()
    
    # Test general chat
    state = {"messages": [HumanMessage(content="Hello, I'm James")],
            "intent": "",
            "status": ""}
    result = workflow.invoke(state)
    response_text = result["messages"][-1].content.lower()
    assert "james" in response_text and ("how can i assist you" in response_text or "how may i help you" in response_text)