# Module for initial seed data. Can be modified to add other kinds of data

import models
from datetime import datetime, timedelta
from database import LocalSession

db = LocalSession()

classes = [
    models.FitnessClass(name='Yoga', date_time = datetime.now() + timedelta(days=2), instructor='Amit Chandra Pal', available_slots=5),
    models.FitnessClass(name='Yoga', date_time = datetime.now() + timedelta(days=3), instructor='Bipin Chandra Pal', available_slots=6)
]

for cls in classes:
    db.add(cls)

db.commit()
db.close()