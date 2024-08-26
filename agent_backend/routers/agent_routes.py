from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from agent_backend.models.ai_agent import AIAgent
from agent_backend.schemas.agent_schemas import (
    AgentCreate,
    AgentUpdate,
    AgentResponse,
    AgentRequest,
)
from agent_backend.utils.auth import get_current_user
from agent_backend.services.agent_service import AgentService
from agent_backend.db.database import get_db
from agent_backend.models.user import User

router = APIRouter()


@router.post("/agents", response_model=AgentResponse)
async def create_agent(
    agent: AgentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return await AgentService.create_agent(db, agent)


@router.get("/agents", response_model=List[AgentResponse])
async def list_agents(
    db: Session = Depends(get_db), current_user: User = Depends(get_current_user)
):
    return await AgentService.list_agents(db)


@router.get("/agents/{agent_id}", response_model=AgentResponse)
async def get_agent(
    agent_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return await AgentService.get_agent(db, agent_id)


@router.put("/agents/{agent_id}", response_model=AgentResponse)
async def update_agent(
    agent_id: int,
    agent: AgentUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return await AgentService.update_agent(db, agent_id, agent)


@router.delete("/agents/{agent_id}", response_model=dict)
async def delete_agent(
    agent_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return await AgentService.delete_agent(db, agent_id)


@router.post("/agents/{agent_id}/process", response_model=str)
async def process_request(
    agent_id: int,
    request: AgentRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    agent = await AgentService.get_agent(db, agent_id)
    # Implement the process_request logic here
    return f"Processed request for agent {agent.name}: {request.input}"
