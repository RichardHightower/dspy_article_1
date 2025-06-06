"""Basic question-answering module from the article."""
import dspy
from config import llm  # This imports and configures the LLM

# Define what your module expects and returns
class SimpleQA(dspy.Signature):
    """Answer a question concisely."""
    question: str = dspy.InputField()
    answer: str = dspy.OutputField()

# Create a module that uses this signature
class QAModule(dspy.Module):
    def __init__(self):
        super().__init__()
        self.predict = dspy.Predict(SimpleQA)

    def forward(self, question):
        return self.predict(question=question)

def main():
    """Run the basic QA example."""
    print("=== Basic Q&A Module Example ===\\n")
    
    # Use it like a regular Python function
    qa = QAModule()
    
    questions = [
        "What is Python?",
        "What are the benefits of using DSPy?",
        "How does chain-of-thought reasoning work?"
    ]
    
    for question in questions:
        print(f"Q: {question}")
        result = qa(question)
        print(f"A: {result.answer}\\n")

if __name__ == "__main__":
    main()
