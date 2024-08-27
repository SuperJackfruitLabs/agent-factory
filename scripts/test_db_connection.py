import os
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

# Use the Docker service name 'db' instead of 'localhost'
DATABASE_URL = os.getenv(
    "DATABASE_URL", "postgresql://user:password@db:5432/ai_agent_db"
)


def test_db_connection():
    try:
        # Create an engine instance
        engine = create_engine(DATABASE_URL)

        # Try to connect to the database
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            print("Successfully connected to the database!")

            # Fetch the result (optional)
            print(result.fetchone())

    except SQLAlchemyError as e:
        print(f"An error occurred while connecting to the database: {e}")


if __name__ == "__main__":
    test_db_connection()
