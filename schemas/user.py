from pydantic import BaseModel

class UserTable(BaseModel):
    name: str
    email: str
    password: str
    username: str