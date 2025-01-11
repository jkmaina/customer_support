# test_product_entities.py
import pytest
from src.llm_classifier import extract_entities, enrich_context

def test_basic_product_extraction():
    """Test basic product and color extraction"""
    state = {
        "input": "What's the price of the blue shirt?",
        "entities": {},
        "context": {}
    }
    
    result = extract_entities(state)
    assert result["entities"].product == "shirt"
    assert result["entities"].color == "blue"

def test_product_without_color():
    """Test extracting product without color mention"""
    state = {
        "input": "How much is the pants?",
        "entities": {},
        "context": {}
    }
    
    result = extract_entities(state)
    assert result["entities"].product == "pants"
    assert result["entities"].color is None

def test_color_without_product():
    """Test extracting color without valid product"""
    state = {
        "input": "Do you have anything in blue?",
        "entities": {},
        "context": {}
    }
    
    result = extract_entities(state)
    assert result["entities"].product is None
    assert result["entities"].color == "blue"

def test_invalid_product():
    """Test with product not in catalog"""
    state = {
        "input": "Looking for a green sofa",
        "entities": {},
        "context": {}
    }
    
    result = extract_entities(state)
    assert result["entities"].product is None
    assert result["entities"].color == "green"

def test_context_enrichment():
    """Test context enrichment with product details"""
    # Test valid product
    state = {
        "input": "Price of blue shirt",
        "entities": {},
        "context": {}
    }
    
    state = extract_entities(state)
    state = enrich_context(state)
    
    assert "product_details" in state["context"]
    assert state["context"]["product_details"]["name"] == "Classic Shirt"
    assert "blue" in state["context"]["product_details"]["available_colors"]
    assert state["context"]["product_details"]["price"] == 29.99

def test_context_enrichment_invalid_product():
    """Test context enrichment with invalid product"""
    state = {
        "input": "Looking for a sofa",
        "entities": {},
        "context": {}
    }
    
    state = extract_entities(state)
    state = enrich_context(state)
    
    # Context should not have product details for invalid product
    assert "product_details" not in state["context"] or not state["context"]["product_details"]

def test_multiple_products():
    """Test handling multiple product mentions"""
    state = {
        "input": "Compare the blue shirt and black pants",
        "entities": {},
        "context": {}
    }
    
    result = extract_entities(state)
    # Should pick up first product mentioned
    assert result["entities"].product in ["shirt", "pants"]
    assert result["entities"].color in ["blue", "black"]

def test_edge_cases():
    """Test various edge cases"""
    # Empty input
    state = {
        "input": "",
        "entities": {},
        "context": {}
    }
    result = extract_entities(state)
    assert result["entities"].product is None
    assert result["entities"].color is None
    
    # Very long input
    state = {
        "input": "I'm looking for a " + "very " * 50 + "blue shirt",
        "entities": {},
        "context": {}
    }
    result = extract_entities(state)
    assert result["entities"].product == "shirt"
    assert result["entities"].color == "blue"
    
    # Special characters
    state = {
        "input": "Looking for a blue shirt!!!???",
        "entities": {},
        "context": {}
    }
    result = extract_entities(state)
    assert result["entities"].product == "shirt"
    assert result["entities"].color == "blue"

if __name__ == "__main__":
    pytest.main([__file__, "-v"])