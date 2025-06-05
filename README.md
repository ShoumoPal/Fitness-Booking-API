# Fitness-Booking-API
### A simple, modular API built with FastAPI, SQLAlchemy, and SQLite, enabling users to browse fitness classes and book slots.
---
<br>

## 🔧 Features
* View available fitness classes
* Book slots for classes
* Retrieve bookings by email
* Seed test data
* Input validation and logging
---

## 🚀 Tech Stack
| **Technology**  | **Purpose**                                        |
|----------------|----------------------------------------------------|
| **FastAPI**    | Web framework for building APIs with Python       |
| **SQLAlchemy** | ORM (Object-Relational Mapper) for database interaction |
| **SQLite**     | Lightweight, file-based database                  |
| **Pydantic**   | Data validation and serialization using Python models |
| **Uvicorn**    | ASGI server for running FastAPI applications      |
---
# 📦 Installation

Clone the repo:
```
git clone https://github.com/ShoumoPal/Fitness-Booking-API.git
```
Change the working directory:
```
cd Fitness-Booking-API/app
```
Create a virtual envionment and activate it
```
python -m venv venv
source venv/Scripts/activate
```
Install the requirements
```
pip install -r requirements.txt
```

### If you would like to see the Olama LLM endpoint I integrated, feel free to download the 'llama3.2:3b' version of the LLM from [here](https://ollama.com/library/llama3.2:3b)
### `NOTE` 
### If you do this then you would need to install Ollama as a whole to check. I have provided screenshots for the endpoint incase you do not want to go through the hassle.
---
# ⚡Requests

Add seed data to the Database
```
python seed.py
```
## Samples
`GET` requests 

* `/classes`

<image src=https://github.com/user-attachments/assets/c1136ab9-a394-4e83-a5a2-769c677469cc  width=50% height=50% />

* `/bookings`

<image src=https://github.com/user-attachments/assets/f4a4e7cb-ed2f-42b5-b988-68752a084177  width=50% height=50% />

---
`POST` requests

* `/book`
  
<image src=https://github.com/user-attachments/assets/54e28537-4062-4aff-b5d4-1058537e9030  width=50% height=50% />

---
`GET` for ollama

<image src=https://github.com/user-attachments/assets/9db541f7-a209-4f60-954d-41546e614373  width=50% height=50% />

### The responses are not the best here since it is a fairly small model, but it works

