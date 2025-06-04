import pytz
from datetime import datetime

classes = [
    {
        'id' : 1,
        'name' : 'Yoga Moment',
        'date_time' : pytz.timezone('Asia/Kolkata').localize(datetime(2025, 2, 2, 10, 20)),
        'instructor' : 'Alice',
        'available_slots' : 3
    },
    {
        'id' : 2,
        'name' : 'Gym Moment',
        'date_time' : pytz.timezone('Asia/Kolkata').localize(datetime(2025, 2, 4, 11, 20)),
        'instructor' : 'Chinu',
        'available_slots' : 1
    }
]

# For later
bookings = []