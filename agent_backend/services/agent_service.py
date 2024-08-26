from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from agent_backend.models.ai_agent import AIAgent
from agent_backend.schemas.agent_schemas import AgentCreate, AgentUpdate


class AgentService:
    @staticmethod
    async def create_agent(db: AsyncSession, agent: AgentCreate):
        db_agent = AIAgent(**agent.dict())
        db.add(db_agent)
        await db.commit()
        await db.refresh(db_agent)
        return db_agent

    @staticmethod
    async def get_agent(db: AsyncSession, agent_id: int):
        result = await db.execute(select(AIAgent).filter(AIAgent.id == agent_id))
        return result.scalar_one_or_none()

    @staticmethod
    async def list_agents(db: AsyncSession):
        result = await db.execute(select(AIAgent))
        return result.scalars().all()

    @staticmethod
    async def update_agent(db: AsyncSession, agent_id: int, agent: AgentUpdate):
        db_agent = await AgentService.get_agent(db, agent_id)
        if db_agent:
            for key, value in agent.dict(exclude_unset=True).items():
                setattr(db_agent, key, value)
            await db.commit()
            await db.refresh(db_agent)
        return db_agent

    @staticmethod
    async def delete_agent(db: AsyncSession, agent_id: int):
        db_agent = await AgentService.get_agent(db, agent_id)
        if db_agent:
            await db.delete(db_agent)
            await db.commit()
        return {"message": "Agent deleted successfully"}
