from fastapi import FastAPI

from routers import base, vectors

app = FastAPI(
    title="Hello",
    openapi_url= "/docs/openapi.json",
    # root_path='/api'
)

app.include_router(
    base.router,
    tags=["base"]
)

app.include_router(
    vectors.router,
    tags=["vectors"]
)