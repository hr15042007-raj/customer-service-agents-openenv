from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field

class ToolCall(BaseModel):
    tool: str
    parameters: Dict[str, Any]

class Observation(BaseModel):
    observation: str
    reward: float
    done: bool
    info: Dict[str, Any]
    available_tools: List[str]
