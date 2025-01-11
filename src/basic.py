# src/basic.py
def process_message(state):
    # Step 2: Write minimal passing code
    state["word_count"] = len(state["input"].split())
    return state