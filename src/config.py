"""Configuration for LLM providers."""
import os
from typing import Optional

from dotenv import load_dotenv
import dspy

# Load environment variables
load_dotenv()

def configure_llm():
    """Configure the LLM based on environment variables."""
    provider = os.getenv("LLM_PROVIDER", "openai").lower()
    model = os.getenv("LLM_MODEL")
    llm : Optional[dspy.LM] = None
    
    if provider == "openai":
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables")
        
        model = model or "gpt-4-turbo-preview"
        llm = dspy.LM(
            model=f"openai/{model}",
            api_key=api_key,
            max_tokens=4096
        )
        
    elif provider == "anthropic":
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY not found in environment variables")
        
        model = model or "claude-3-opus-20240229"
        llm = dspy.LM(
            model=f"anthropic/{model}",
            api_key=api_key,
            max_tokens=4096
        )
        
    elif provider == "ollama":
        base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
        model = model or "phi3:latest"
        llm = dspy.LM(
            model=f"ollama_chat/{model}",
            base_url=base_url,
            max_tokens=2048  # Smaller for local models
        )
        
    else:
        raise ValueError(f"Unknown LLM provider: {provider}")
    
    # Configure DSPy with the selected LLM
    dspy.settings.configure(lm=llm)
    
    print(f"Configured DSPy with {provider} provider using {model} model")
    return llm

# Initialize on import
llm = configure_llm()
