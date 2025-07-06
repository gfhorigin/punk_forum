from fastapi import FastAPI, Response, Request
from fastapi.middleware.cors import CORSMiddleware
import hashlib
import models
import db_utils
import responses
import token_manager

tm = token_manager.TokenManager()

app = FastAPI()

# временно ------
db = db_utils.DB()
db.add_user('d82494f05d6917ba02f7aaa29689ccb444bb73f20380876cb05d1f37537b7892')
db.add_name('admin')
# ---------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:5173'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/login")
def login(info: models.UserModel, response: Response):
    email = info.email
    password = info.password
    if hashlib.sha256((email + password).encode()).hexdigest() in db.get_users():
        tm.set_token(response=response, info={"message": "good"})
        return response, responses.success_response()

    return responses.invalid_credentials()


@app.post("/registration")
def registration(info: models.UserModel, response: Response):
    email = info.email
    password = info.password

    if email in db.get_names():
        return responses.email_exists()
    db.add_name(email)
    db.add_user(hashlib.sha256((email + password).encode()).hexdigest())
    tm.set_token(response=response, info={"message": "good"})

    return response, responses.success_response()


@app.get("/check-auth")
def check_auth(request: Request):
    print(request.cookies)
    if request.cookies == {}:
        return responses.invalid_auth()

    token = request.cookies.get(tm.get_cookie_name())

    return responses.success_response()
