"""Code analysis pipeline from the article."""

import dspy


class CodeAnalysisPipeline(dspy.Module):
    def __init__(self):
        super().__init__()

        # Module 1: Understand what the code does
        self.understand = dspy.Predict("code -> description")

        # Module 2: Identify potential issues
        self.find_issues = dspy.ChainOfThought("description -> issues")

        # Module 3: Suggest fixes
        self.suggest_fixes = dspy.Predict("code, issues -> suggestions")

    def forward(self, code):
        # Step 1: Understand the code
        description = self.understand(code=code).description

        # Step 2: Find issues (with reasoning)
        issues = self.find_issues(description=description).issues

        # Step 3: Suggest improvements
        suggestions = self.suggest_fixes(code=code, issues=issues).suggestions

        return {
            "description": description,
            "issues": issues,
            "suggestions": suggestions,
        }


def main():
    """Run the code analyzer example."""
    print("=== Code Analysis Pipeline Example ===\\n")

    # Analyze some problematic code
    analyzer = CodeAnalysisPipeline()

    code_samples = [
        {
            "name": "Division by Zero Risk",
            "code": """
def calculate_average(numbers):
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)
""",
        },
        {
            "name": "Memory Leak Potential",
            "code": """
class DataProcessor:
    def __init__(self):
        self.cache = []
    
    def process(self, data):
        result = expensive_operation(data)
        self.cache.append(result)  # Never cleared!
        return result
""",
        },
        {
            "name": "SQL Injection Risk",
            "code": """
def get_user(user_id):
    query = f"SELECT * FROM users WHERE id = {user_id}"
    return db.execute(query)
""",
        },
    ]

    for sample in code_samples:
        print(f"Analyzing: {sample['name']}")
        print(f"Code:\\n{sample['code']}")

        analysis = analyzer(sample["code"])

        print(f"\\nWhat it does: {analysis['description']}")
        print(f"\\nIssues found: {analysis['issues']}")
        print(f"\\nSuggestions: {analysis['suggestions']}")
        print("\\n" + "=" * 70 + "\\n")


if __name__ == "__main__":
    main()
