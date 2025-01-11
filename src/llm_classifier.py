# llm_classifier.py
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from typing import Optional

class ProductEntity(BaseModel):
    product: Optional[str] = None
    color: Optional[str] = None

def lookup_product(product_name):
    """Look up product details from database"""
    catalog = {
        "shirt": {
            "name": "Classic Shirt",
            "available_colors": ["red", "blue", "white", "black"],
            "price": 29.99
        },
        "pants": {
            "name": "Casual Pants",
            "available_colors": ["black", "navy", "khaki"],
            "price": 49.99
        },
        "jacket": {
            "name": "Winter Jacket",
            "available_colors": ["black", "green", "brown"],
            "price": 89.99
        }
    }
    return catalog.get(product_name.lower() if product_name else "", {})

def extract_entities(state):
    """Extract product and color entities using structured output"""
    llm = ChatOpenAI(temperature=0, model="gpt-4o-mini").with_structured_output(ProductEntity)
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", """Extract the product and color from the query.        
        Only extract products from this list: shirt, pants, jacket"""),
        ("human", "{query}")  
    ])
    
    chain = prompt | llm
    state["entities"] = chain.invoke({"query": state["input"]})  
    return state

def enrich_context(state):
    """Enrich context with product details"""
    if not state["entities"] or not state["entities"].product:
        state["context"] = {}  # Initialize empty context if no product
        return state
        
    state["context"] = {
        "product_details": lookup_product(state["entities"].product)
    }
    return state

def process_query(query):
    """Process a single query through the pipeline"""
    state = {"input": query}
    state = extract_entities(state)
    state = enrich_context(state)
    return state

def main():
    test_queries = [
        "I want a blue shirt",
        "Do you have any red jackets?",
        "Show me black pants",
        "What colors do you have?",
    ]
    
    print("Processing queries...\n")
    for query in test_queries:
        print(f"Query: {query}")
        try:
            result = process_query(query)
            print(f"Extracted Entities: {result['entities']}")
            if result['context']:
                print(f"Product Details: {result['context']['product_details']}")
            print()
        except Exception as e:
            print(f"Error processing query: {str(e)}\n")

if __name__ == "__main__":
    main()