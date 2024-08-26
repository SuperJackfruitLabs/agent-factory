import pytest
from sqlalchemy.ext.asyncio import AsyncSession
from agent_backend.models.ai_agent import AIAgent
from agent_backend.schemas.agent_schemas import AgentCreate
from agent_backend.services.agent_service import AgentService


@pytest.fixture
async def db_session():
    db = next(get_db())
    try:
        yield db
    finally:
        db.close()


@pytest.mark.asyncio
async def test_create_and_retrieve_agent(db_session: AsyncSession):
    agent_data = AgentCreate(
        name="Test Agent",
        description="A test agent",
        agent_type="test",
        tools=["tool1", "tool2"],
        model_name="gpt-3.5-turbo",
        temperature=0.7,
    )

    created_agent = await AgentService.create_agent(db_session, agent_data)
    assert created_agent.id is not None

    retrieved_agent = await AgentService.get_agent(db_session, created_agent.id)
    assert retrieved_agent.name == agent_data.name
    assert retrieved_agent.description == agent_data.description
    assert retrieved_agent.agent_type == agent_data.agent_type
    assert retrieved_agent.tools == agent_data.tools
    assert retrieved_agent.model_name == agent_data.model_name
    assert retrieved_agent.temperature == agent_data.temperature


@pytest.mark.asyncio
async def test_update_agent(db_session: AsyncSession):
    agent_data = AgentCreate(
        name="Original Agent",
        description="Original description",
        agent_type="original",
        tools=["tool1"],
        model_name="gpt-3.5-turbo",
        temperature=0.7,
    )

    created_agent = await AgentService.create_agent(db_session, agent_data)

    update_data = {
        "name": "Updated Agent",
        "description": "Updated description",
        "agent_type": "updated",
        "tools": ["tool1", "tool2"],
        "model_name": "gpt-4",
        "temperature": 0.8,
    }

    updated_agent = await AgentService.update_agent(
        db_session, created_agent.id, update_data
    )

    assert updated_agent.name == update_data["name"]
    assert updated_agent.description == update_data["description"]
    assert updated_agent.agent_type == update_data["agent_type"]
    assert updated_agent.tools == update_data["tools"]
    assert updated_agent.model_name == update_data["model_name"]
    assert updated_agent.temperature == update_data["temperature"]


@pytest.mark.asyncio
async def test_delete_agent(db_session: AsyncSession):
    agent_data = AgentCreate(
        name="Agent to Delete",
        description="This agent will be deleted",
        agent_type="test",
        tools=["tool1"],
        model_name="gpt-3.5-turbo",
        temperature=0.7,
    )

    created_agent = await AgentService.create_agent(db_session, agent_data)

    await AgentService.delete_agent(db_session, created_agent.id)

    with pytest.raises(
        Exception
    ):  # Adjust the exception type based on your implementation
        await AgentService.get_agent(db_session, created_agent.id)
