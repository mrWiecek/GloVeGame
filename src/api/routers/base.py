from fastapi import APIRouter, Request

router = APIRouter()

@router.get("/")
async def root():
    return {"Hello": "World"}

@router.get("/hello")
async def hello():
    return {"is": "ok"}

@router.get("/app")
def read_main(request: Request):
    return {"message": "Hello World", "root_path": request.scope.get("root_path")}
