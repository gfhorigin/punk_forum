import os

from dotenv import load_dotenv

from authx import AuthX, AuthXConfig


class TokenManager:
    def __init__(self):
        load_dotenv()

        self.config = AuthXConfig()
        self.config.JWT_SECRET_KEY = os.getenv('SECRET_KEY')
        self.config.JWT_ACCESS_COOKIE_NAME = "token"
        self.config.JWT_TOKEN_LOCATION = ['cookies']

        self.security = AuthX(config=self.config)

    def gety_token(self,info=None):
        return  self.security.create_access_token(uid='my_id', data=info)

    def set_token(self, response, info=None):
        token = self.security.create_access_token(uid='my_id', data=info)

        response.set_cookie(
            key=self.config.JWT_ACCESS_COOKIE_NAME,
            value=token,
            httponly=True,
            max_age=3600,
            path="/",
            secure =False
        )


    def get_security(self):
        return self.security

    def get_cookie_name(self):
        return self.config.JWT_ACCESS_COOKIE_NAME

