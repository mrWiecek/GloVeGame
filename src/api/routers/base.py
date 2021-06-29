from fastapi import APIRouter, Request

router = APIRouter()

payload = {
	"userId": 1,
	"id": 1,
	"title": "delectus aut autem",
	"completed": False
}

@router.get("/")
async def root():
    return payload

@router.get("/hello")
async def hello():
    return {"is": "ok"}

@router.get("/app")
def read_main(request: Request):
    return {"message": "Hello World", "root_path": request.scope.get("root_path")}
