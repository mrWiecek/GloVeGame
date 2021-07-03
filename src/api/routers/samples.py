import logging
from fastapi import APIRouter, Body, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List
from server.models import AnalogyModel
from server.database import analogies_collection

router = APIRouter()


@router.post("/", response_description="Add new analogy", response_model=AnalogyModel)
async def create_analogy(analogy: AnalogyModel = Body(...)):
    analogy = jsonable_encoder(analogy)
    new_analogy = await analogies_collection.insert_one(analogy)
    created_analogy = await analogies_collection.find_one({"_id": new_analogy.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_analogy)


@router.get(
    "/", response_description="List all analogies", response_model=List[AnalogyModel]
)
async def list_analogies():
    analogies = await analogies_collection.find().to_list(1000)
    return analogies