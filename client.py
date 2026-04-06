# OpenEnv Client for Customer Service Agents (CSA-001)
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, ConfigDict, Field

# This client is used by the OpenEnv benchmark to communicate with the environment
class Action(BaseModel):
    model_config = ConfigDict(extra='allow')
    tool: str = Field(description="The name of the tool to be called")
    parameters: Dict[str, Any] = Field(default_factory=dict, description="Arguments for the tool")
    thought: Optional[str] = Field(None, description="The reasoning behind this action")

class Observation(BaseModel):
    model_config = ConfigDict(extra='allow')
    observation: str = Field(description="The tool output or natural language observation")
    step_count: int = Field(default=0)
    history: List[Dict[str, Any]] = Field(default_factory=list)
    available_tools: List[str] = Field(default_factory=list)
