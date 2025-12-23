"""Simple startup server code."""

import argparse

import uvicorn


def main() -> None:
    """Startup server."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", default=8000)
    parser.add_argument("--dev", action="store_true")
    parser.add_argument("--path", default="time_flow.app:app")
    args = parser.parse_args()
    uvicorn.run(args.path, host=args.host, port=args.port, reload=args.dev)


if __name__ == "__main__":
    main()
