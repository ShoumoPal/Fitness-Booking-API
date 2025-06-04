from fastapi import FastAPI, Query, HTTPException
from database import classes, bookings
from utils import convert_timezone
from AI import get_llm_response, get_llm_answers
from models import BookingRequest, BookingResponse
import pytz
from datetime import datetime
from pydantic import EmailStr

app = FastAPI()

@app.get('/classes')
def get_classes():
    return classes

@app.get('/AI_GET')
def get_llm_classes():
    return get_llm_response()

@app.put('/askAI')
def ask_AI(question : str = Query(...)):
    return get_llm_answers(question)

@app.post('/book', response_model=BookingResponse)
def bookslot(request : BookingRequest):
    cls = next((c for c in classes if c['id'] == request.class_id), None)

    if not cls:
        raise HTTPException(status_code=400, detail='Class not found...')

    if cls['available_slots'] <= 0:
        raise HTTPException(status_code=400, detail='No slots available...')

    booking = {
        'class_id' : request.class_id,
        'client_name' : request.client_name,
        'client_email' : request.client_email,
        'booking_time' : pytz.timezone('Asia/Kolkata').localize(datetime.now())
    }

    bookings.append(booking)
    cls['available_slots'] -= 1

    return BookingResponse(**booking)

@app.get('/bookings')
def getbookings(email : EmailStr = Query(...)):
    currBookings = [booking for booking in bookings if booking['client_email'] == email]

    if not currBookings:
        raise HTTPException(status_code=400, detail='No bookings found...')

    return currBookings
    
