from pydantic import BaseModel

class add(BaseModel):
    Title: int
    Guest: str
    Topic: str