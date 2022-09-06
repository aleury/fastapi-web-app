import fastapi
from fastapi.requests import Request
from fastapi_chameleon import template

from viewmodels.home.index import IndexViewModel

router = fastapi.APIRouter()


@router.get("/")
@template()
def index(request: Request):
    vm = IndexViewModel(request)
    return vm.to_dict()


@router.get("/about")
@template("home/about.pt")
def about():
    return {}
