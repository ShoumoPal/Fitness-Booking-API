import ollama
from database import classes
import json

get_prompts = {
    'user' : f'You are given a list of classes below in JSON format: \n{classes}' \
               'Give me a one line answer about the types of classes available. Be concise and quirky',
    'system' : 'You are an assistant who is very knowledgable on the Fitness domain and very precise with your answers.'
}
QA_prompts = {
    'system' : 'You are an assistant who is very knowledgable on the Fitness domain and very precise with your answers.'
}

def get_llm_response():
    response = ollama.chat(model='llama3.2',
                           messages=[{'role':'system', 'content':get_prompts['system']},
                                 {'role':'user', 'content': get_prompts['user']}])
    
    result = response['message']['content']
    return(result[:1000])

def get_llm_answers(question : str) -> str:
    response = ollama.chat(model='llama3.2',
                           messages=[{'role':'system', 'content':QA_prompts['system']},
                                          {'role':'user', 'content':question}])
    result = response['message']['content']
    return result[:2000]

print(get_llm_response())