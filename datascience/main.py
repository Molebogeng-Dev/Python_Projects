from podcast_template import Template
from fastapi import FastAPI, HTTPException
from schema import Add

data=Template().update_all


app= FastAPI()
@app.get('/')
def home():
    return data

@app.get('/{id}')
def welcome(id: int, q: str):
    if q == 'Guest':
        try:
            return f'Welcome {data[q].iloc[id]}'
        except:
            raise HTTPException(status_code=404, detail='Item not found')
    else: 
        return f'Upcoming event: {data.iloc[len(data) - 1]}'

@app.post('/update')
def update(add: Add):
    add = {'Title': input('Title: '), 'Guest': input('Guest: '), 'Topic': input('Topic: ')}
    return f'new podcast details added: {add}'