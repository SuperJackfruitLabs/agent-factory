from pydantic import BaseModel, ConfigDict
from typing import Optional, List


class AgentCreate(BaseModel):
    name: str
    description: Optional[str] = None
    agent_type: str
    tools: List[str] = []
    model_name: str = "gpt-3.5-turbo"
    temperature: float = 0.7

    model_config = ConfigDict(protected_namespaces=())


class AgentUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    agent_type: Optional[str] = None
    tools: Optional[List[str]] = None
    model_name: Optional[str] = None
    temperature: Optional[float] = None

    model_config = ConfigDict(protected_namespaces=())


class AgentResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    agent_type: str
    tools: List[str]
    model_name: str
    temperature: float

    model_config = ConfigDict(protected_namespaces=())


class AgentRequest(BaseModel):
    input: str
