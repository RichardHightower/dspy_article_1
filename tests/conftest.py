"""Pytest configuration to load test environment."""

import pytest
import os
import sys
from dotenv import load_dotenv

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))


@pytest.fixture(autouse=True, scope="session")
def setup_test_environment():
    """Load test environment variables."""
    # Load the test .env file
    test_env_path = os.path.join(os.path.dirname(__file__), "..", ".env.test")
    load_dotenv(test_env_path, override=True)

    # Import config after loading test env to initialize DSPy with test LLM
    # ruff: noqa: E402
    import config  # noqa: F401

    yield
