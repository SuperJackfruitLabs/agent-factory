import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor


def run_fastapi():
    subprocess.run(
        [
            "poetry",
            "run",
            "uvicorn",
            "agent_backend.main:app",
            "--reload",
            "--port",
            "8000",
        ]
    )


def run_mkdocs():
    subprocess.run(
        [
            "poetry",
            "run",
            "mkdocs",
            "serve",
            "--dev-addr",
            "localhost:8001",
        ]
    )


def main():
    with ThreadPoolExecutor(max_workers=2) as executor:
        fastapi_future = executor.submit(run_fastapi)
        mkdocs_future = executor.submit(run_mkdocs)

        try:
            fastapi_future.result()
            mkdocs_future.result()
        except KeyboardInterrupt:
            print("Shutting down servers...")
            sys.exit(0)


if __name__ == "__main__":
    main()
