# AI Agent Framework

AI Agent Framework is a scalable and flexible system for building AI-enabled assistants. It provides a robust backend infrastructure to create, manage, and deploy intelligent agents for various applications.

## Features

- 🚀 Scalable Architecture: Designed to handle from personal projects to enterprise-level applications.
- 🧠 Flexible AI Model Integration: Easily integrate and switch between different AI models.
- 🔌 Extensible Plugin System: Enhance functionality through a modular plugin architecture.
- 🔒 Strong Security & Privacy: Built-in features to ensure data protection and user privacy.
- 🌐 RESTful API: Well-documented API for seamless integration with various frontend applications.

## Getting Started

### Prerequisites

- Python 3.12+
- Poetry
- Docker and Docker Compose (for running the full stack)
- Node.js and npm (for frontend development)

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/Super-Jackfruit-Labs/agent-factory.git
   cd agent-factory
   ```

2. Install backend dependencies:
   ```
   cd backend
   poetry install
   ```

3. Set up pre-commit hooks:
   ```
   poetry run pre-commit install
   ```

4. Install frontend dependencies:
   ```
   cd ../frontend
   npm install
   ```

### Running the Application

To run the full stack using Docker Compose:

```
docker-compose up --build
```

This will start:
- FastAPI backend server at `http://localhost:8000`
- PostgreSQL database
- Next.js frontend at `http://localhost:3000`

For backend development, you can run the FastAPI server and MkDocs documentation server simultaneously:

```
cd backend
poetry run dev
```

This will start:
- FastAPI server at `http://localhost:8000`
- MkDocs documentation server at `http://localhost:8001`

For frontend development:

```
cd frontend
npm run dev
```

This will start the Next.js development server at `http://localhost:3000`.

## Development

- Run backend tests: `cd backend && poetry run pytest`
- Format backend code: `cd backend && poetry run black .`
- Lint backend code: `cd backend && poetry run flake8`

## Documentation

Our documentation is built using MkDocs and served in the Docker environment. You can view it at `http://localhost:8001` when running the full stack.

For local documentation development:

```
bash
cd docs
pip install -r requirements.txt
mkdocs serve
```

Then visit `http://localhost:8000` in your browser.

## Contributing

We welcome contributions to the AI Agent Framework! Please see our [Contributing Guidelines](CONTRIBUTING.md) for more details on how to get started.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Project Status

This project is currently in active development. We are in the process of implementing core features and establishing the project structure.
