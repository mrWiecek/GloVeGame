from fastapi import FastAPI

from routers import base

app = FastAPI(
    title="Hello",
    openapi_url= "/docs/openapi.json",
    root_path='/api'
)

app.include_router(
    base.router,
    tags=["base"]
)