from bson import ObjectId
from pydantic import BaseModel, Field


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


class AnalogyModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    wordIs: str
    wordTo: str
    wordAsIs: str
    wordAsTo: str
    is_valid: bool

    class Config:

        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {

            "example": {
                "wordIs": "king",
                "wordTo": "man",
                "wordAsIs": "queen",
                "wordAsTo": "woman",
                "is_valid": True
            }

        }

class ClosestWords(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    wordOrg: str
    wordClose: str
    is_valid: bool

    class Config:

        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {

            "example": {
                "wordOrg": "king",
                "wordClose": "man",
                "is_valid": True
            }

        }