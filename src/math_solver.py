"""Chain-of-thought math solver from the article."""

import dspy
from config import configure_llm


class MathReasoning(dspy.Signature):
    """Solve a math problem step by step."""

    problem: str = dspy.InputField()
    reasoning: str = dspy.OutputField(desc="Step-by-step solution")
    answer: str = dspy.OutputField(desc="Final answer")


class MathSolver(dspy.Module):
    def __init__(self):
        super().__init__()
        # ChainOfThought makes the model show its work
        self.solve = dspy.ChainOfThought(MathReasoning)

    def forward(self, problem):
        return self.solve(problem=problem)


def main():
    """Run the math solver example."""
    print("=== Chain-of-Thought Math Solver Example ===\\n")
    
    # Configure the language model
    configure_llm()

    # Solve problems
    solver = MathSolver()

    problems = [
        "A bakery sold 45 croissants in the morning and 28 in the afternoon. "
        "If each croissant costs $3.50, what was the total revenue?",
        "If a train travels at 80 km/h for 2.5 hours, then slows to 60 km/h "
        "for another 1.5 hours, what is the total distance traveled?",
        "A rectangular garden is 15 meters long and 8 meters wide. "
        "If we want to put a fence around it that costs $12 per meter, "
        "what will be the total cost?",
    ]

    for i, problem in enumerate(problems, 1):
        print(f"Problem {i}: {problem}")
        result = solver(problem)
        print(f"\\nReasoning: {result.reasoning}")
        print(f"Answer: {result.answer}\\n")
        print("=" * 70 + "\\n")


if __name__ == "__main__":
    main()
