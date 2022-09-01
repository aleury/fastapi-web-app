import fastapi

from fastapi_chameleon import template

router = fastapi.APIRouter()


@router.get("/")
@template()
def index(user: str = 'anon'):
    return {"username": user}


@router.get("/about")
def about():
    return {}
