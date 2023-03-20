from typing import List, Optional
from pydantic import BaseModel, Field
from contracts.pyObjectId import *


class CarInDB(BaseModel):
    id: PyObjectId = Field(alias="_id")
    name: str = Field(...)
    type: str = Field(...) 
    seat: str = Field(...)
    fuel: str = Field(...)
    desc: str = Field(...)
    features: List[str] = Field(...)
    requiredDocuments: List[str] = Field(...)
    collateral: int = Field(...)
    price: int = Field(...)
    address: object = Field(...)
    images: List[object] = Field(...)
    ownerId: str = Field(...)
    ownerUsername: str = Field(...)

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class CarModel(BaseModel):
    name: str = Field(...)
    type: str = Field(...) 
    seat: str = Field(...)
    fuel: str = Field(...)
    desc: str = Field(...)
    features: List[str] = Field(...)
    requiredDocuments: List[str] = Field(...)
    collateral: int = Field(...)
    price: int = Field(...)
    address: object = Field(...)
    images: List[object] = Field(...)
    ownerId: str = Field(...)
    ownerUsername: str = Field(...)

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "MITSUBISHI 2019",
                "type": "xe-tu-lai",
                "seat": "2",
                "fuel": "diesel",
                "desc": "short description",
                "features": ["map", "gps", "tire"],
                "requiredDocuments": ["cmnd", "gplx"],
                "collateral": 500,
                "price": 1000,
                "address":{"district":"","ward":"","addressDetail":""},
                "images": [],
                "ownerId": "5f9f1b9b9c9d440017a1b1b5"
            }
        }
# car: Type, version, price,
class UpdateCarInDB(BaseModel):
    name: Optional[str]
    type: Optional[str]
    seat: Optional[str]
    fuel: Optional[str]
    desc: Optional[str]
    features: List[str]
    requiredDocuments:  List[str]
    collateral: Optional[int]
    price: Optional[int]
    address: object = Field(...)
    images: List[str] = Field(...)
    ownerId: Optional[str]

    


    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "MITSUBISHI 2019",
                "type": "xe-tu-lai",
                "seat": "2",
                "battCapa": "32,26 kwh",
                "fuel": "diesel",
                "desc": "short description",
                "features": ["map", "gps", "tire"],
                "requiredDocuments": ["cmnd", "gplx"],
                "collateral": 500,
                "price": 1000,
                "address":{"district":"","ward":"","addressDetail":""},
                "images": [],
                "ownerId": "5f9f1b9b9c9d440017a1b1b5"
            }
        }


