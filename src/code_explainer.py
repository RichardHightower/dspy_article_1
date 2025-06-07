"""Code explanation module from the article."""

import dspy


class CodeExplanation(dspy.Signature):
    """Explain what a piece of code does."""

    code: str = dspy.InputField(desc="The code to explain")
    language: str = dspy.InputField(desc="Programming language")
    explanation: str = dspy.OutputField(desc="Clear explanation of the code")
    key_concepts: str = dspy.OutputField(desc="Main concepts used")


class CodeExplainer(dspy.Module):
    def __init__(self):
        super().__init__()
        self.predict = dspy.Predict(CodeExplanation)

    def forward(self, code, language="Python"):
        return self.predict(code=code, language=language)


def main():
    """Run the code explainer example."""
    print("=== Code Explainer Module Example ===\\n")

    # Try it out
    explainer = CodeExplainer()

    sample_codes = [
        {
            "code": """
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
""",
            "language": "Python",
        },
        {
            "code": """
function quickSort(arr) {
    if (arr.length <= 1) return arr;
    const pivot = arr[Math.floor(arr.length / 2)];
    const left = arr.filter(x => x < pivot);
    const right = arr.filter(x => x > pivot);
    return [...quickSort(left), pivot, ...quickSort(right)];
}
""",
            "language": "JavaScript",
        },
    ]

    for sample in sample_codes:
        print(f"Code ({sample['language']}):")
        print(sample["code"])

        result = explainer(sample["code"], sample["language"])
        print(f"Explanation: {result.explanation}")
        print(f"Key concepts: {result.key_concepts}\\n")
        print("-" * 50 + "\\n")


if __name__ == "__main__":
    main()
