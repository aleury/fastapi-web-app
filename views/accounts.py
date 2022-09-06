import fastapi
from fastapi.requests import Request

from viewmodels import accounts

router = fastapi.APIRouter()


@router.get("/account")
def index(request: Request):
    vm = accounts.IndexViewModel(request)
    return vm.to_dict()


@router.get("/account/register")
def register(request: Request):
    vm = accounts.RegisterViewModel(request)
    return vm.to_dict()


@router.get("/account/login")
def login(request: Request):
    vm = accounts.LoginViewModel(request)
    return vm.to_dict()


@router.get("/account/logout")
def logout():
    return {}
