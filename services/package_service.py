from datetime import datetime

from data.package import Package
from data.release import Release


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


def get_package_by_name(package_name: str) -> Package | None:
    package = Package(
        name=package_name,
        summary="This is the summary",
        home_page="https://fastapi.tiangolo.com",
        lic="MIT",
        author_name="Sebastián Ramírez",
        description="Full details here!",
    )
    return package


def get_latest_release_for_package(package_name: str) -> Release | None:
    release = Release("1.2.0", datetime.now())
    return release
