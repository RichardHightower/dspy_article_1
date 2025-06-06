"""Unit tests for DSPy modules."""
import pytest
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from basic_qa import QAModule
from code_explainer import CodeExplainer
from math_solver import MathSolver
from code_analyzer import CodeAnalysisPipeline

def test_qa_module():
    """Test basic QA functionality."""
    qa = QAModule()
    result = qa("What is Python?")
    
    assert hasattr(result, 'answer')
    assert isinstance(result.answer, str)
    assert len(result.answer) > 0

def test_code_explainer():
    """Test code explanation functionality."""
    explainer = CodeExplainer()
    code = "def hello(): return 'Hello, World!'"
    result = explainer(code, "Python")
    
    assert hasattr(result, 'explanation')
    assert hasattr(result, 'key_concepts')
    assert isinstance(result.explanation, str)
    assert isinstance(result.key_concepts, str)

def test_math_solver():
    """Test math solver functionality."""
    solver = MathSolver()
    problem = "What is 2 + 2?"
    result = solver(problem)
    
    assert hasattr(result, 'reasoning')
    assert hasattr(result, 'answer')
    assert isinstance(result.reasoning, str)
    assert isinstance(result.answer, str)

def test_code_analyzer():
    """Test code analysis pipeline."""
    analyzer = CodeAnalysisPipeline()
    code = '''
def divide(a, b):
    return a / b
'''
    result = analyzer(code)
    
    assert isinstance(result, dict)
    assert 'description' in result
    assert 'issues' in result
    assert 'suggestions' in result
    assert all(isinstance(v, str) for v in result.values())

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
