# project_package

This package contains the core agent implementation used by the Community Risk Intelligence Agent project.

## Content
- `agents.py` - core agent classes (LocalStubLLM, EventBus, RiskAnalysisAgent, etc.)
- `tests/test_agents_module.py` - basic unit tests for the package

## Install locally
```bash
pip install -r requirements.txt
pip install -e .
```

## Usage example
```py
from project_package.agents import LocalStubLLM, RiskAnalysisAgent, EventBus
llm = LocalStubLLM()
bus = EventBus()
ra = RiskAnalysisAgent('test', bus, llm)
```

