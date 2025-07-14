from pydantic import BaseModel


class UserModel(BaseModel):
    email: str
    password: str


class UserRegistrationModel(BaseModel):
    nickname: str
    unique_name: str
    email: str
    password: str
