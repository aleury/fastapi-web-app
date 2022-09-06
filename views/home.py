import fastapi
from fastapi.requests import Request
from fastapi_chameleon import template

from viewmodels import home
from viewmodels import shared

router = fastapi.APIRouter()


@router.get("/")
@template()
def index(request: Request):
    vm = home.IndexViewModel(request)
    return vm.to_dict()


@router.get("/about")
@template("home/about.pt")
def about(request: Request):
    vm = shared.ViewModelBase(request)
    return vm.to_dict()
