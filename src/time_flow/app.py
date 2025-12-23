"""App file."""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root() -> str:
    """Root endpoint."""
    return "Hello, user"
