from typing import List, Optional
from pydantic import BaseModel, Field, EmailStr
from contracts.pyObjectId import *




class UserInDB(BaseModel):
    id: PyObjectId = Field(alias="_id")
    username: str = Field(...)
    email: str = Field(...)
    password: str = Field(...)
    role: str = Field(...)
    fullName: str = Field(...)
    phone: str = Field(...)
    address: str = Field(...)
    vendorState: str = Field(...)
    imagesID: List[object] = Field(...)
    createdAt: str = Field(...)
    
    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class UserRegister(BaseModel):
    username: str = Field(...)
    email: str = Field(...)
    password: str = Field(...)
    fullName: str = Field(...)
    phone: str = Field(...)
    address: str = Field(...)
    vendorState: str = Field(...)
    imagesID: List[object] = Field(...)
    
    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "username": "user_01",
                "email": "user_01@gmail.com",
                "password": "user_01",
                "fullName": "user_01",
                "phone": "19001781",
                "address": "Hai Ba Trung",
                "vendorState": "pending",
                "imagesID": []
            }
        }

class UserModel(BaseModel):
    username: str = Field(...)
    email: str = Field(...)
    password: str = Field(...)
    role: str = Field(...)
    vendor_state:  str = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "username": "ADMIN",
                "email": "admin@gmail.com",
                "password": "admin",
                "role": "",
                "vendor_state": ""
            }
        }



class UpdateUserModel(BaseModel):
    username: str = Field(...)
    email: str = Field(...)
    password: str = Field(...)
    role: str = Field(...)
    vendor_state:  str = Field(...)

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "username": "ADMIN",
                "email": "admin@gmail.com",
                "password": "admin",
                "role": "",
                "vendor_state": ""
            }
        }


class UserLogin(BaseModel):
    email: str = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "email": "admin@gmail.com",
                "password": "admin",
            }
        }


# vendor

class VendorModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    username: str = Field(...)
    address: str = Field(...)
    phone: int = Field(...)
    carName: str = Field(...)
    role: str = Field(...)
    vendor_state:  str = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "username": "ADMIN",
                "address": "Hai Ba Trung",
                "phone": "19001781",
                "carName": "admin",
                "role": "",
                "vendor_state": ""
            }
        }


class UpdateVendorModel(BaseModel):
    username: str = Field(...)
    address: str = Field(...)
    phone: int = Field(...)
    carName: str = Field(...)
    role: str = Field(...)
    vendor_state:  str = Field(...)

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "username": "ADMIN",
                "address": "Hai Ba Trung",
                "phone": "19001781",
                "carName": "admin",
                "role": "",
                "vendor_state": ""
            }
        }


class ListUser(BaseModel):
    id: str = Field(...)
    username: str = Field(...)
    email: str = Field(...)
    password: str = Field(...)
    role: str = Field(...)
    createdAt: str = Field(...)


