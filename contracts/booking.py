from pydantic import BaseModel, Field
from contracts.pyObjectId import *



class BookingModel(BaseModel):
    carId: str = Field(...)
    userId: str = Field(...)
    startDate: str = Field(...)
    endDate: str = Field(...)
    total: int = Field(...)


    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class BookingInDB(BaseModel):
    id: PyObjectId = Field(alias="_id")
    carId: str = Field(...)
    userId: str = Field(...)
    carName: str = Field(...)
    ownerId: str = Field(...)
    ownerUsername: str = Field(...)
    userId: str = Field(...)
    startDate: str = Field(...)
    endDate: str = Field(...)
    status: str = Field(...)
    total: int = Field(...)
    createdAt: str = Field(...)



    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

