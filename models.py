from pydantic import BaseModel


class UserModel(BaseModel):
    email: str
    password: str


class UserRegistrationModel:
    nickname: str
    unique_name: str
    email: str
    password: str
