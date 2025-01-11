# The Complete LangGraph Blueprint - Customer Support AI Agent

[![The Complete LangGraph Blueprint - Book Cover](https://m.media-amazon.com/images/I/71yR8ReePcL._SY466_.jpg)](https://www.amazon.com/Complete-LangGraph-Blueprint-Business-Success-ebook/dp/B0DP69QV7K)

Welcome to the official repository for **The Complete LangGraph Blueprint**, authored by James Karanja Maina. This repository contains the customer support AI agent project from Chapter 19, demonstrating practical implementation of LangGraph concepts through Test-Driven Development (TDD).

## About the Book 📚

This book guides you through creating 50+ AI agents for real-world business applications using LangGraph and other cutting-edge AI tools. Whether you're a beginner or an experienced developer, you'll learn to harness AI for innovation and success.

### Why Buy This Book? 🎯

- **Exclusive Knowledge**: Master the techniques for building 50+ AI agents
- **Hands-On Learning**: Follow detailed examples and exercises step by step
- **Real-World Applications**: Solve practical business problems with AI
- **Expert Guidance**: Learn from industry experience in AI and automation

👉 [Get your copy now on Amazon!](https://www.amazon.com/Complete-LangGraph-Blueprint-Business-Success-ebook/dp/B0DP69QV7K)

### Key Book Features 🚀

- **50+ AI Agents**: Build and customize AI agents with dynamic decision-making
- **Graph-Based AI Workflows**: Create workflows using nodes, edges, states, and conditions
- **LLM Integration**: Leverage Large Language Models like GPT-4
- **Tool Nodes**: Integrate APIs and external systems
- **Memory & Persistence**: Implement short-term and long-term memory
- **Use Cases**: Apply skills across customer service, healthcare, and finance
- **Practical Exercises**: Reinforce learning with hands-on coding

---

## Chapter 19 Project: Customer Support AI Agent

This repository contains the complete code for the customer support AI agent discussed in Chapter 19. The project demonstrates Test-Driven Development (TDD) in building AI applications.

### Learning Objectives
- Understand TDD in AI applications
- Build modular AI agents with LangChain and LangGraph
- Write and maintain test suites for AI components
- Manage state in conversational AI

### Prerequisites
- Python 3.10 or higher
- Basic understanding of Python and testing
- OpenAI API key
- The Complete LangGraph Blueprint book (recommended)

### Project Structure
```
customer_support/
├── src/
│   ├── basic.py                    # Basic message processing
│   ├── conversation_memory.py      # Conversation state management
│   ├── llm_classifier.py           # LLM-based entity extraction
│   ├── support_agent.py            # Main agent implementation
├── tests/
│   ├── test_basic.py              # Basic functionality tests
│   ├── test_conversation_memory.py # State management tests
│   ├── test_llm_classifier.py      # Entity extraction tests
│   ├── test_support_agent.py       # Main agent tests
├── .env                            # Environment configuration
├── pytest.ini                      # Pytest configuration
├── requirements.txt                # Project dependencies
├── setup.py                        # Package setup file
```

### Setup Instructions

1. Clone the repository and create a virtual environment:
```bash
git clone <repository-url>
cd customer_support
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure your OpenAI API key:
   - Create a `.env` file in the project root
   - Add your API key: `OPENAI_API_KEY=your_api_key_here`

4. Run the tests:
```bash
pytest
```

### Key Components

1. **Intent Classification** (Chapter 19.5)
   - Located in `src/support_agent.py`
   - Classifies customer queries into specific intents
   - Handles order status, product inquiries, and general chat

2. **State Management** (Chapter 19.4)
   - Located in `src/conversation_memory.py`
   - Manages conversation history and context
   - Implements turn counting and message tracking

3. **Entity Extraction** (Chapter 19.5)
   - Located in `src/llm_classifier.py`
   - Processes product names, colors, and other entities
   - Includes product catalog functionality

4. **Main Agent Workflow** (Chapter 19.3)
   - Implements complete customer support workflow
   - Uses LangGraph for state management
   - Demonstrates proper error handling

### Running the Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_support_agent.py

# Run with verbose output
pytest -v

# Run with coverage report
pytest --cov=src
```

### Common Issues and Solutions

1. **API Key Errors**
   - Verify OpenAI API key in `.env`
   - Check python-dotenv configuration

2. **Test Failures**
   - Ensure all dependencies are installed
   - Verify internet access for API calls
   - Check OpenAI model availability

3. **State Management Issues**
   - Verify state dictionary keys
   - Check message history maintenance

### Next Steps

1. Read Chapter 20 for advanced agent patterns
2. Try the exercises at the end of Chapter 19
3. Implement additional features suggested in the book:
   - New intents
   - Extended product catalog
   - Enhanced error handling
   - Conversation summarization
   - User authentication

## Additional Resources

- [Official Book Website](https://www.amazon.com/Complete-LangGraph-Blueprint-Business-Success-ebook/dp/B0DP69QV7K)
- [LangChain Documentation](https://python.langchain.com/docs/get_started/introduction)
- [LangGraph Documentation](https://python.langchain.com/docs/langgraph)
- [Python Testing with pytest](https://docs.pytest.org/en/stable/)

## Support

For book-related questions and discussions:
- Leave a review on Amazon
- Follow the author on Twitter for updates @zavora_ai

For technical issues with this repository:
- Open an issue on GitHub
- Check the notes in Chapter 19
- Review the relevant sections in the book

Remember: Success with this project comes from following the TDD cycle as outlined in Chapter 19:
1. Write a failing test
2. Write minimal code to make it pass
3. Refactor while keeping tests green

Happy coding, and don't forget to grab your copy of **The Complete LangGraph Blueprint** for the complete guide! 📚