from fastapi import FastAPI, Response, Request, Depends
from fastapi.middleware.cors import CORSMiddleware
from authx_extra.oauth2 import MiddlewareOauth2
import hashlib
import models
import db_utils
import responses
import token_manager

tm = token_manager.TokenManager()

app = FastAPI()

db = db_utils.DB()
# временно ------
#
# db.add_user('d82494f05d6917ba02f7aaa29689ccb444bb73f20380876cb05d1f37537b7892')
# db.add_name('admin')
# ---------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:5173'],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

app.add_middleware(
    MiddlewareOauth2,
    providers={
        'google': {
            'keys': 'https://www.googleapis.com/oauth2/v3/certs',
            'issuer': 'https://accounts.google.com',
            'audience': '852159111111-xxxxxx.apps.googleusercontent.com',
        }
    },
    public_paths={'/'},
)


@app.post("/login")
def login(info: models.UserModel, response: Response):
    email = info.email
    password = info.password
    login_hash = hashlib.sha256((email + password).encode()).hexdigest()
    if db.hash_check(login_hash=login_hash):
        tm.set_token(response=response, uid=email)
        return response, responses.success_response()

    return responses.invalid_credentials()


@app.post("/registration")
def registration(info: models.UserRegistrationModel, response: Response):
    email = info.email
    password = info.password

    if db.email_exists(email):
        return responses.email_exists()
    if db.unique_exists(info.unique_name):
        return responses.unique_exists()

    login_hash = hashlib.sha256((email + password).encode()).hexdigest()

    db.add_user(
        login_hash=login_hash,
        email=email,
        nickname=info.nickname,
        unique_name=info.unique_name
    )
    tm.set_token(response=response, uid=email)

    return response, responses.success_response()


@app.get("/check-auth")
def check_auth(request: Request):  # payload: TokenPayload = Depends(tm.get_security().access_token_required)):
    token = request.cookies.get(tm.get_cookie_name())
    if token is None:
        return responses.invalid_auth()

    token = token[2:-1]
    payload = tm.get_security()._decode_token(token)

    return responses.success_response(data=db.get_user_auth_info_by_email(payload.sub))
