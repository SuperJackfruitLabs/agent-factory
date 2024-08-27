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

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/Super-Jackfruit-Labs/agent-factory.git
   cd agent-factory
   ```

2. Install dependencies:
   ```
   poetry install
   ```

3. Set up pre-commit hooks:
   ```
   poetry run pre-commit install
   ```

### Running the Application

To run both the FastAPI server and MkDocs documentation server simultaneously:

```
poetry run dev
```

This will start:
- FastAPI server at `http://localhost:8000`
- MkDocs documentation server at `http://localhost:8001`

## Development

- Run tests: `poetry run pytest`
- Format code: `poetry run black .`
- Lint code: `poetry run flake8`

## Documentation

Our documentation is built using MkDocs. You can view it locally by running:

```
poetry run mkdocs serve
```

Then visit `http://localhost:8000` in your browser.

## Contributing

We welcome contributions to the AI Agent Framework! Please see our [Contributing Guidelines](CONTRIBUTING.md) for more details on how to get started.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Project Status

This project is currently in active development. We are in the process of implementing core features and establishing the project structure.
