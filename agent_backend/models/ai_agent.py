from sqlalchemy import Column, Integer, String, Float, JSON
from agent_backend.db.database import Base


class AIAgent(Base):
    __tablename__ = "ai_agents"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, nullable=True)
    agent_type = Column(String)
    tools = Column(JSON)
    model_name = Column(String)
    temperature = Column(Float)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "agent_type": self.agent_type,
            "tools": self.tools,
            "model_name": self.model_name,
            "temperature": self.temperature,
        }
