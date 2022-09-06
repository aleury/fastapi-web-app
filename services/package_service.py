def package_count() -> int:
    return 274_000


def release_count() -> int:
    return 2_234_847


def latest_packages(limit: int = 5) -> list:
    packages = [
        {"id": "fastapi", "summary": "A great web framework."},
        {"id": "uvicorn", "summary": "Your favorite ASGI server."},
        {"id": "httpx", "summary": "Requests for the async world."},
    ]
    return packages[:limit]
