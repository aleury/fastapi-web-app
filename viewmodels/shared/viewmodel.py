from fastapi.requests import Request


class ViewModelBase:
    def __init__(self, request: Request):
        self.request: Request = request
        self.error: str | None = None
        self.user_id: int | None = None
        self.is_logged_in: bool = False

    def to_dict(self) -> dict:
        return self.__dict__
