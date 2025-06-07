"""Main entry point for all DSPy examples."""

import sys
from pathlib import Path

# Check if .env.test exists and use it if no .env is configured
env_path = Path(__file__).parent.parent / ".env"
test_env_path = Path(__file__).parent.parent / ".env.test"

if not env_path.exists() and test_env_path.exists():
    from dotenv import load_dotenv

    load_dotenv(test_env_path)

# Import config to initialize DSPy - must be after env setup
# This import is required to initialize DSPy with the LLM
# ruff: noqa: E402
import config  # noqa: F401


def print_header(title):
    """Print a formatted header."""
    print("\\n" + "=" * 70)
    print(f"{title:^70}")
    print("=" * 70 + "\\n")


def main():
    """Run all examples from the article."""
    print_header("DSPy Examples - Stop Wrestling with Prompts")

    # Import and run each example
    examples = [
        ("Basic Q&A Module", "basic_qa"),
        ("Code Explainer", "code_explainer"),
        ("Chain-of-Thought Math Solver", "math_solver"),
        ("Code Analysis Pipeline", "code_analyzer"),
        ("Advanced Features", "advanced_examples"),
    ]

    for title, module_name in examples:
        try:
            print_header(title)
            module = __import__(module_name)
            module.main()
            print("\\n" + "-" * 70)
        except KeyboardInterrupt:
            print("\\n\\nExiting examples...")
            sys.exit(0)
        except Exception as e:
            print(f"Error running {module_name}: {e}")
            print("Continuing to next example...")

    print_header("All Examples Complete!")
    print("Explore the individual modules in src/ to see how each works.")
    print(
        "Check out the DSPy documentation for more: https://github.com/stanfordnlp/dspy"
    )


if __name__ == "__main__":
    main()
