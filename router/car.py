from fastapi import APIRouter,Body,status, HTTPException
from contracts.car import CarInDB, UpdateCarInDB, CarModel
from fastapi.encoders import jsonable_encoder
from db import db
from fastapi.responses import JSONResponse
from typing import Optional, List
from bson import ObjectId

router = APIRouter()

#Create a car
@router.post("/car/create", response_model=CarInDB)
async def create_car(car: CarModel=Body(...)):
    car = car.dict()
    new_car = await db['Cars'].insert_one(car)
    created_car = await db["Cars"].find_one({"_id": new_car.inserted_id})
    return created_car

#Get all car for admin
@router.get("/car/all", response_model=List[CarInDB])
async def list_cars():
    cars = await db["Cars"].find().to_list(1000)
    return cars

#Get all car for admin
@router.get("/car/list-new", response_model=List[CarInDB])
async def list_cars():
    cars = await db["Cars"].find().to_list(5)
    return cars


#Get all car for vendor
@router.get("/car/all/{id}", response_model=List[CarInDB])
async def list_cars(id: str):
    cars = await db["Cars"].find({"ownerId": id}).to_list(1000)
    return cars


#Get a car by id
@router.get("/car/{id}", response_model=CarInDB)
async def get_id(id: str):
    if (car := await db["Cars"].find_one({"_id": ObjectId(id)})) is not None:
        return car
    raise HTTPException(status_code=404, detail="Car {id} not found")


#Update a car
@router.put("/car/{id}", response_model=CarInDB)
async def update_id(id: str, car: UpdateCarInDB = Body(...)):
    car = {k: v for k, v in car.dict().items() if v is not None}

    if len(car) >= 1:
        update_result = await db["Cars"].update_one({"_id": ObjectId(id)}, {"$set": car})

        if update_result.modified_count == 1:
            if (
                updated_car := await db["car"].find_one({"_id": ObjectId(id)})
            ) is not None:
                return updated_car

    if (existing_car := await db["Cars"].find_one({"_id": ObjectId(id)})) is not None:
        return existing_car

    raise HTTPException(status_code=404, detail="Car {id} not found")

#Delete a car
@router.delete("/car/{id}")
async def delete_car(id: str):
    delete_result = await db["Cars"].delete_one({"_id": ObjectId(id)})

    if delete_result.deleted_count == 1:
        return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Deleted successfully"})

    raise HTTPException(status_code=404, detail=f"Car {id} not found")


#Search cars
@router.get("/car-searching", response_model=List[CarInDB])
async def search_cars(
    type: Optional[str] = None,
    seat: Optional[str] = None,
    district: Optional[str] = None,
    ward: Optional[str] = None,
):
    car = {}
    if type:
        car["type"] = type
    if seat:
        car["seat"] = seat
    if district:
        car["address.district"] = district
    if ward:
        car["address.ward"] = ward

    cars = await db["Cars"].find(car).to_list(1000)
    return cars
