from fastapi import FastAPI, Query
from database import classes
from utils import convert_timezone
from AI import get_llm_response, get_llm_answers

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