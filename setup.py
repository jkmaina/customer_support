from setuptools import setup, find_packages

setup(
    name="customer_support",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pytest",
        "pytest-asyncio",
        "langchain",
        "openai",
        "python-dotenv",
        "langgraph"
    ],
)