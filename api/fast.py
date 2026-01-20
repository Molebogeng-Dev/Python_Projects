from fastapi import FastAPI
from pydantic import BaseModel
import pandas

df= pandas.read_json('credentials.json')
data= df['installed']

class Credentials(BaseModel):
    client_id: str
    project_id: str
    auth_uri: str
    token_uri: str
    a_p_url: str
    client_secret: str
    redirect_uris: str

app= FastAPI()

@app.get('/')
def home(name: str = ''):
    return {'greeting': f'Welcome {name}'} 


@app.get('/credentials')
def credentials():
    return data

@app.put('/update')
def update()
