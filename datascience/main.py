from podcast_template import Template
from fastapi import FastAPI

data=Template().update_all

# print(data)


app= FastAPI()

@app.get('/{id}')
def home():
    return data

@app.get('/{id}')
def welcome(id: int ):
    return f'Welcome {data['Guest'].iloc[id]}'
    