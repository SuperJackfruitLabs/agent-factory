# Contributing to AI Agent Framework

We're excited that you're interested in contributing to the AI Agent Framework! This document outlines the process for contributing to this project.

## Getting Started

1. Fork the repository on GitHub.
2. Clone your fork locally:
   ```
   git clone https://github.com/your-username/agent-factory.git
   cd agent-factory
   ```
3. Set up your development environment as described in the README.md.

## Making Changes

1. Create a new branch for your feature or bug fix:
   ```
   git checkout -b feature/your-feature-name
   ```
2. Make your changes and commit them with a clear commit message:
   ```
   git commit -m "Add feature: your feature description"
   ```
3. Push your changes to your fork:
   ```
   git push origin feature/your-feature-name
   ```
4. Submit a pull request to the main repository.

## Code Style

- For the backend:
  - Follow PEP 8 guidelines for Python code.
  - Use Black for code formatting (this is enforced by pre-commit hooks).
  - Use type hints where appropriate.
- For the frontend:
  - Follow the Next.js and React best practices.
  - Use ESLint and Prettier for code formatting.

## Testing

- For the backend:
  - Add unit tests for new features or bug fixes.
  - Ensure all tests pass before submitting a pull request.
- For the frontend:
  - Consider adding component tests using React Testing Library.

## Pull Request Process

1. Ensure your code adheres to the project's style guidelines.
2. Update the README.md with details of changes to the interface, if applicable.
3. Increase the version numbers in any examples files and the README.md to the new version that this Pull Request would represent.
4. Your pull request will be reviewed by maintainers. Be open to feedback and be prepared to make changes if requested.

## Reporting Bugs

- Use the issue tracker to report bugs.
- Describe the bug in detail, including steps to reproduce.
- Include information about your environment (OS, Python version, Node.js version, etc.).

## Requesting Features

- Use the issue tracker to suggest new features.
- Clearly describe the feature and its potential benefits to the project.
- Be open to discussion about the feature's implementation.

## Development Environment

- We use Docker and Docker Compose for local development. Make sure you have them installed.
- The project includes a backend built with FastAPI and a frontend built with Next.js. Familiarize yourself with both if you plan to work on the full stack.

Thank you for your interest in improving the AI Agent Framework!

Finally, let's update the developer documentation (backend/docs/developer-guide/contributing.md):

# Developer Guide: Contributing

## Setting Up the Development Environment

1. Ensure you have Python 3.12+, Poetry, Docker, and Docker Compose installed on your system.

2. Clone the repository:
   ```
   git clone https://github.com/SuperJackfruitLabs/agent-factory.git
   cd agent-factory
   ```

3. Install backend dependencies:
   ```
   cd backend
   poetry install
   ```

4. Set up pre-commit hooks:
   ```
   poetry run pre-commit install
   ```

5. Install frontend dependencies:
   ```
   cd ../frontend
   npm install
   ```

## Running the Application

### Using Docker Compose (Recommended for Full Stack)

To run the entire stack (backend, frontend, and database):

```
docker-compose up --build
```

This will start:
- FastAPI backend server at `http://localhost:8000`
- PostgreSQL database
- Next.js frontend at `http://localhost:3000`

### For Backend Development

Run the FastAPI server and MkDocs documentation server:

```
cd backend
poetry run dev
```

This starts:
- FastAPI server at `http://localhost:8000`
- MkDocs documentation server at `http://localhost:8001`

### For Frontend Development

Run the Next.js development server:

```
cd frontend
npm run dev
```

This starts the Next.js server at `http://localhost:3000`.

## Code Style and Quality

### Backend
- We use Black for code formatting. Run `poetry run black .` in the backend directory to format your code.
- Flake8 is used for linting. Run `poetry run flake8` in the backend directory to check your code.
- Use type hints in all Python code.

### Frontend
- Follow Next.js and React best practices.
- Use ESLint and Prettier for code formatting.

## Testing

### Backend
- Write unit tests for all new features and bug fixes.
- Run tests using `poetry run pytest` in the backend directory.
- Ensure all tests pass before submitting a pull request.

### Frontend
- Consider adding component tests using React Testing Library.

## Documentation

- Update the MkDocs documentation in the `backend/docs` directory for any new features or changes.
- Run `poetry run mkdocs serve` in the backend directory to view the documentation locally.

## Database Migrations

- We use SQLAlchemy for database operations. If you make changes to the database models, you'll need to create and apply migrations.

## Submitting Changes

1. Create a new branch for your feature or bug fix.
2. Make your changes and commit them with clear, descriptive commit messages.
3. Push your changes to your fork on GitHub.
4. Submit a pull request to the main repository.
5. Be prepared to respond to feedback and make changes if requested.

## Questions and Support

If you have any questions or need support while contributing, please open an issue on GitHub or reach out to the maintainers.

Thank you for contributing to the AI Agent Framework!
