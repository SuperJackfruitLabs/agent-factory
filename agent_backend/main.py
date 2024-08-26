from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from agent_backend.routers import agent_routes, auth_routes  # Add this import
from agent_backend.db.database import engine
from agent_backend.models.ai_agent import Base
from agent_backend.utils.error_handlers import (
    AppException,
    app_exception_handler,
    http_exception_handler,
)

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Agent Framework API",
    description="Backend API for the AI Agent Framework",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(agent_routes.router, prefix="/api/v1")
app.include_router(auth_routes.router, prefix="/api/v1/auth")  # Add this line

app.add_exception_handler(AppException, app_exception_handler)
app.add_exception_handler(HTTPException, http_exception_handler)


@app.get("/")
async def root():
    return {"message": "Welcome to the AI Agent Framework API"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
