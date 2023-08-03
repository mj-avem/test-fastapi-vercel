from pydantic import BaseModel

class PersonDto(BaseModel):
    name: str
    sex: str
    age: int
