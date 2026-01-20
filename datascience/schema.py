from pydantic import BaseModel

class Add(BaseModel):
    Title: str
    Guest: str
    Topic: str