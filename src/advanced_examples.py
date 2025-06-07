"""Advanced DSPy features mentioned in the article."""

import dspy
from pydantic import BaseModel, Field
from typing import List
import asyncio
from config import configure_llm


# Structured Output Example
class AnalysisOutput(BaseModel):
    """Structured output for sentiment analysis."""

    sentiment: str = Field(description="positive, negative, or neutral")
    confidence: float = Field(description="Confidence score between 0 and 1")
    key_phrases: List[str] = Field(description="Important phrases from the text")


class SentimentAnalyzer(dspy.Module):
    def __init__(self):
        super().__init__()
        self.analyze = dspy.Predict("text -> analysis")

    def forward(self, text):
        result = self.analyze(text=text)
        # In production, you'd parse this into the Pydantic model
        return result


# Tool Integration Example
def search_documentation(query: str) -> str:
    """Simulated documentation search."""
    # In real implementation, this would search actual docs
    docs = {
        "dspy": "DSPy is a framework for programming language models",
        "signature": "Signatures define inputs and outputs for modules",
        "chainofthought": "Chain-of-thought prompting shows reasoning steps",
    }

    query_lower = query.lower()
    for key, value in docs.items():
        if key in query_lower:
            return value
    return "No documentation found for that query."


class DocumentationHelper(dspy.Module):
    def __init__(self):
        super().__init__()
        self.answer = dspy.ChainOfThought("question -> answer")

    def forward(self, question):
        # DSPy can use the tool when needed
        return self.answer(question=question)


# Optimization Example
def create_optimized_qa():
    """Example of how to optimize a module (simplified)."""
    from src.basic_qa import QAModule

    # In practice, you'd have training examples
    # Example training data (not used in this simplified demo)
    # training_examples = [
    #     dspy.Example(
    #         question="What is Python?",
    #         answer="Python is a high-level programming language known for its simplicity and readability.",
    #     ),
    #     dspy.Example(
    #         question="What is DSPy?",
    #         answer="DSPy is a framework for programming language models declaratively.",
    #     ),
    # ]

    # Create and compile an optimized version
    qa = QAModule()

    # Note: Full optimization requires more setup
    # This is a simplified example
    print(
        "Module optimization example prepared (full optimization requires training data)"
    )
    return qa


# Async Operations Example
async def analyze_many_texts(texts: List[str]):
    """Analyze multiple texts concurrently."""
    analyzer = SentimentAnalyzer()

    async def analyze_one(text):
        # In production, this would be truly async
        return analyzer(text)

    tasks = [analyze_one(text) for text in texts]
    results = await asyncio.gather(*tasks)
    return results


def main():
    """Demonstrate advanced features."""
    print("=== Advanced DSPy Features ===\\n")
    
    # Configure the language model
    configure_llm()

    # 1. Structured Output
    print("1. Structured Output Example:")
    analyzer = SentimentAnalyzer()
    result = analyzer("DSPy makes working with LLMs so much easier and more reliable!")
    print(f"Analysis: {result.analysis}\\n")

    # 2. Tool Usage
    print("2. Tool Integration Example:")
    helper = DocumentationHelper()
    result = helper("What is a DSPy signature?")
    print(f"Answer: {result.answer}\\n")

    # 3. Optimization
    print("3. Optimization Example:")
    create_optimized_qa()
    print("(See code for optimization setup)\\n")

    # 4. Async Operations
    print("4. Async Operations Example:")
    texts = [
        "This product is amazing!",
        "Terrible experience, would not recommend.",
        "It's okay, nothing special.",
    ]

    # Run async example
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        results = loop.run_until_complete(analyze_many_texts(texts))
        print("Analyzed multiple texts concurrently")
        for text, result in zip(texts, results):
            print(f"  Text: {text[:30]}... -> {result.analysis}")
    finally:
        loop.close()


if __name__ == "__main__":
    main()
