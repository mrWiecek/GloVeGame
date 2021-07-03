from fastapi import FastAPI
from routers import base, samples, vectors



app = FastAPI(
    title="Hello",
    openapi_url="/docs/openapi.json",
    # root_path='/api'
)

app.include_router(
    base.router,
    prefix='/api',
    tags=["base"]
)

app.include_router(
    vectors.router,
    prefix='/api',
    tags=["vectors"]
)

app.include_router(
    samples.router,
    prefix='/api/analogy',
    tags=["samples"]
)
