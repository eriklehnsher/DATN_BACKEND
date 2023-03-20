from fastapi import APIRouter, Body
from contracts.booking import BookingModel,BookingInDB
from db import db
from fastapi.encoders import jsonable_encoder
from fastapi import Body, HTTPException, status, Depends
from bson import ObjectId
from typing import List
import datetime
import smtplib
from email.message import EmailMessage
import ssl

router = APIRouter()
email_address = "nhokti98dan@gmail.com"
email_password= "etvlpekrpjtnhbxu"

@router.post("/booking/create/{id}", response_model=BookingInDB)
async def create_booking(id: str, booking_info:BookingModel = Body(...) ):
  booking_info =booking_info.dict()
  bookings = db["Bookings"].find({"carId": id, "status": "approved"})
  async for booking in bookings:
    if booking_info["startDate"] < booking["endDate"] and booking_info["endDate"] > booking["startDate"]:
      raise HTTPException(status_code=400, detail="Car is not available at this time")
  

  car = await db["Cars"].find_one({"_id": ObjectId(id)})
  ownerID = car["ownerId"]
  carName = car["name"]
  ownerUsername = car["ownerUsername"]
  now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

  booking_info["ownerId"] = ownerID
  booking_info["ownerUsername"] = ownerUsername
  booking_info["status"] = "pending"
  booking_info["createdAt"] = now
  booking_info["carName"] = carName

  result = await db["Bookings"].insert_one(booking_info)
  created_booking = await db["Bookings"].find_one({"_id": result.inserted_id})
  return created_booking
  
@router.post("/booking/approve/{id}", response_model=BookingModel)
async def approve_booking(id: str):
  booking = await db["Bookings"].find_one({"_id": ObjectId(id)})
  if booking is None:
      raise HTTPException(
          status_code=status.HTTP_404_NOT_FOUND, detail="booking not found")
  else:
      await db["Bookings"].update_one({"_id": ObjectId(id)}, {"$set": { "status": "approved"}})
      updated_booking = await db["Bookings"].find_one({"_id": ObjectId(id)})
      user= await db["Users"].find_one({"_id": ObjectId(updated_booking["userId"])})

      #send email to user

      msg = EmailMessage()
      msg['Subject'] = 'Đặt xe thành công'
      msg['From'] = email_address
      msg['To'] = user["email"]
      body = "Yêu cầu đặt xe của bạn đã được duyệt"+"\n" + "Tên xe: " + updated_booking["carName"] +"\nTên chủ xe: " + updated_booking["ownerUsername"] +"\n" + "Ngày bắt đầu: " + updated_booking["startDate"] + "\n" + "Ngày kết thúc: " + updated_booking["endDate"] + "\n" + "Tổng tiền: " + str(updated_booking["total"])+".000vnd" + "\n" + "\n" + "Cảm ơn bạn đã sử dụng dịch vụ của chúng tôi"
      msg.set_content(body)
      with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_address, email_password)
        smtp.sendmail(email_address, user["email"], msg.as_string())


      return updated_booking

@router.post("/booking/reject/{id}", response_model=BookingModel)
async def reject_booking(id: str):
  booking = await db["Bookings"].find_one({"_id": ObjectId(id)})
  if booking is None:
      raise HTTPException(
          status_code=status.HTTP_404_NOT_FOUND, detail="booking not found")
  else:
      await db["Bookings"].update_one({"_id": ObjectId(id)}, {"$set": { "status": "rejected"}})
      updated_booking = await db["Bookings"].find_one({"_id": ObjectId(id)})
      user= await db["Users"].find_one({"_id": ObjectId(updated_booking["userId"])})

      #send email to user
      msg= EmailMessage()
      msg['Subject'] = 'Đặt xe thất bại'
      msg['From'] = email_address
      msg['To'] = user["email"]
      body = "Yêu cầu đặt xe của bạn đã bị từ chối"+"\n" + "Tên xe: " + updated_booking["carName"] +"\nTên chủ xe: " + updated_booking["ownerUsername"] +"\n" + "Ngày bắt đầu: " + updated_booking["startDate"] + "\n" + "Ngày kết thúc: " + updated_booking["endDate"] + "\n" + "Tổng tiền: " + str(updated_booking["total"])+".000vnd" + "\n" + "\n" + "Cảm ơn bạn đã sử dụng dịch vụ của chúng tôi"  
      msg.set_content(body)
      with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_address, email_password)
        smtp.sendmail(email_address, user["email"], msg.as_string())




      return updated_booking


#get all booking for user
@router.get("/booking/user/{userId}", response_model=List[BookingInDB])
async def get_all_bookings(userId: str):
  bookings = await db["Bookings"].find({"userId": userId}).to_list(1000)
  return bookings

#get all booking for vendor
@router.get("/booking/vendor/{ownerId}", response_model=List[BookingInDB])
async def get_all_bookings(ownerId: str):
  bookings = await db["Bookings"].find({"ownerId": ownerId}).to_list(1000)
  return bookings

#get all booking for admin
@router.get("/booking/admin", response_model=List[BookingInDB])
async def get_all_bookings():
  bookings = await db["Bookings"].find().to_list(1000)
  return bookings