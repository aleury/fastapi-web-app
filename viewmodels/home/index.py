from fastapi.requests import Request

from services import package_service, user_service
from viewmodels.shared.viewmodel import ViewModelBase


class IndexViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)
        self.user_count: int = user_service.user_count()
        self.release_count: int = package_service.release_count()
        self.package_count: int = package_service.package_count()
        self.packages: list = package_service.latest_packages()
