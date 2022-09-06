import fastapi
from fastapi.requests import Request
from fastapi_chameleon import template

from viewmodels import packages

router = fastapi.APIRouter()


@router.get('/project/{package_name}')
@template("packages/details.pt")
def details(package_name: str, request: Request):
    vm = packages.DetailsViewModel(package_name, request)
    return vm.to_dict()
