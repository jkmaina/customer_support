# test_conversation_state.py
from src.conversation_memory import add_message

def test_conversation_memory():
    state = {
        "messages": [],
        "context": {},
        "turn_count": 0
    }
    
    # Add a message
    state = add_message(state, "user", "Hello")
    assert len(state["messages"]) == 1
    assert state["turn_count"] == 1
    
    # Add system response
    state = add_message(state, "system", "Hi there!")
    assert len(state["messages"]) == 2
    assert state["turn_count"] == 1