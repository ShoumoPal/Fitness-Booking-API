from fastapi import Depends, FastAPI, Query, HTTPException
from database import engine, LocalSession
from AI import get_llm_response
import models, schemas
import pytz
from datetime import datetime
from pydantic import EmailStr
from sqlalchemy.orm import Session
from typing import List
from app_logger import loggerUtil
from database import getDB

# Create tables in DB
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# GET Classes endpoint
@app.get('/classes', response_model=List[schemas.FitnessClassResponse])
def get_classes(db : Session = Depends(getDB)):
    classes = db.query(models.FitnessClass).all()

    loggerUtil.info('Fetched all available classes from DB...')
    
    if not classes or len(list(classes)) == 0:
        raise HTTPException(status_code=400, detail='No classes found...')

    return classes

# POST/Create booking endpoint
@app.post('/book', response_model=schemas.BookingResponse)
def bookslot(request : schemas.BookingRequest, db : Session = Depends(getDB)):
    cls = db.query(models.FitnessClass).filter(models.FitnessClass.id == request.class_id).first()

    loggerUtil.info(f'Booking attempt for class id : {request.class_id} by {request.client_name}')

    if not cls:
        loggerUtil.info(f'Booking attempt failed for class id : {request.class_id} by {request.client_name}... Class not found..')
        raise HTTPException(status_code=400, detail='Class not found...')

    if cls.available_slots <= 0:
        loggerUtil.info(f'Booking attempt failed for class id : {request.class_id} by {request.client_name}... No slots available in {cls.name} class with id : {cls.id}..')
        raise HTTPException(status_code=400, detail='No slots available...')

    booking = models.Bookings(
        class_id = request.class_id,
        client_name = request.client_name,
        client_email = request.client_email,
        booking_time = pytz.timezone('Asia/Kolkata').localize(datetime.now())
    )

    cls.available_slots -= 1

    db.add(booking)
    db.commit()
    db.refresh(cls)
    db.refresh(booking)

    return booking

# GET booking endpoint for a particular email
@app.get('/bookings', response_model=List[schemas.BookingResponse])
def getbookings(email : EmailStr = Query(...), db : Session = Depends(getDB)):
    currBookings = db.query(models.Bookings).filter(models.Bookings.client_email == str(email))

    if not currBookings or len(list(currBookings)) == 0:
        raise HTTPException(status_code=400, detail='No bookings found...')

    return currBookings

# Incase all bookings are needed to be shown
@app.get('/allbookings', response_model=List[schemas.BookingResponse])
def getbookings(email : EmailStr = Query(...), db : Session = Depends(getDB)):
    currBookings = db.query(models.Bookings).all()
    if not currBookings:
        raise HTTPException(status_code=400, detail='No bookings found...')

    return currBookings

# Ollama LLM response bot 
@app.get('/AI_GET')
def get_llm_classes(db : Session = Depends(getDB)):
    bookings = db.query(models.Bookings).all()
    classes = db.query(models.FitnessClass).all()
    return get_llm_response(classes[:], bookings[:])
    
