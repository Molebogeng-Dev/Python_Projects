from podcast_template import Template
from fastapi import FastAPI, HTTPException

data=Template().update_all

# print(data)


app= FastAPI()

@app.get('/')
def home():
    return data

@app.get('/{id}')
def welcome(id: int ):
    try:
        return f'Welcome {data['Guest'].iloc[id]}'
    except:
        raise HTTPException(status_code=404, detail='Item not found')