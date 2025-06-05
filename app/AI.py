# Additional module for utilizing an LLM (llama3.2) to generate data summaries or anything related

import ollama
from typing import List
from models import FitnessClass, Bookings

#from database import classes
QA_prompts = {
    'system' : 'You are an assistant who is very knowledgable on the Fitness domain and very precise with your answers.'
}

def get_llm_response(class_list : List[FitnessClass], booking_list : List[Bookings]):
    get_prompts = {
        'user' : f'You are given a list of classes below in JSON format: Class list:\n{class_list}\nBooking List: {booking_list}\n' \
               'Give me a short answer about the types of classes available and the available seats given by \'available_slots\' in each class.'
               'Make the answer in such a way that mimics a sales person',
        'system' : 'You are an assistant who is very knowledgable on the Fitness domain and very precise with your answers. You also do not make things up'
    }
    response = ollama.chat(model='llama3.2', messages=[{'role':'system', 'content':get_prompts['system']},
                                                       {'role':'user', 'content':get_prompts['user']}])
    result = response['message']['content']
    return result[:2000]

# def get_llm_answers(question : str) -> str:
#     response = ollama.chat(model='llama3.2',
#                            messages=[{'role':'system', 'content':QA_prompts['system']},
#                                           {'role':'user', 'content':question}])
#     result = response['message']['content']
#     return result[:2000]

#print(get_llm_response())