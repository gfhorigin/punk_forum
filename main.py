from fastapi import FastAPI, Response, Request, Cookie
import hashlib
import models
import db_utils
import responses
import token_manager

tm = token_manager.TokenManager()

app = FastAPI()

db = db_utils.DB()
db.add_user('d82494f05d6917ba02f7aaa29689ccb444bb73f20380876cb05d1f37537b7892')
db.add_name('admin')


@app.post("/login")
def login(info: models.UserModel, response: Response):
    email = info.email
    password = info.password
    if hashlib.sha256((email + password).encode()).hexdigest() in db.get_users():
        token = tm.gety_token({"message": "good"})

        response.set_cookie(
            key=tm.get_cookie_name(),
            value="token",
            httponly=True,
            max_age=3600,
            path="/",
            samesite="Lax",
            secure=False

        )
        return responses.success_response()

    return responses.invalid_credentials()


@app.post("/registration")
def registration(info: models.UserModel, response: Response):
    email = info.email
    password = info.password

    if email in db.get_names():
        return responses.email_exists()
    db.add_name(email)
    db.add_user(hashlib.sha256((email + password).encode()).hexdigest())
    tm.set_token(response)

    return responses.success_response()


@app.get("/check-auth")
def check_auth(request: Request):
    token = request.cookies.get(tm.get_cookie_name())
    print(request.cookies)
    print(request.headers)
    print(token, tm.get_cookie_name())
    return {'message': tm.get_cookie_name(),
            'info': token}
