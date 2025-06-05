# Module to handle schemas related to tasks

from pydantic import BaseModel, EmailStr, Field
from datetime import datetime

class BookingRequest(BaseModel):
    class_id : int = Field(..., gt=0)
    client_name : str = Field(..., min_length=5, max_length=30)
    client_email : EmailStr

class BookingResponse(BookingRequest):
    booking_time : datetime

class FitnessClassResponse(BaseModel):
    id : int
    name : str
    date_time : datetime
    instructor : str
    available_slots : int

    class Config:
        orm_mode = True