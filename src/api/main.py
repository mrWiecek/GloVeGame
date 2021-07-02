# import os
from fastapi import FastAPI
from os
from bson import ObjectId
import motor.motor_asyncio

from routers import base, vectors

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb+srv://root:rootpassword@mongodb/samples?retryWrites=true&w=majority&authSource=admin')
db = client.samples

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

app = FastAPI(
    title="Hello",
    openapi_url= "/docs/openapi.json",
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