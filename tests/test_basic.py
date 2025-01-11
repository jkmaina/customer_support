# tests/test_basic.py
from src.basic import process_message


def test_message_processor():
    # Step 1: Write the failing test
    state = {"input": "Hello world", "word_count": 0}
    result = process_message(state)
    assert result["word_count"] == 2

def test_message_processor_empty():
    state = {"input": "", "word_count": 0}
    result = process_message(state)
    assert result["word_count"] == 0