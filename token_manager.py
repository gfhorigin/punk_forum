from authx import AuthX, AuthXConfig
import config


class TokenManager:
    def __init__(self):

        self.config = AuthXConfig()
        self.config.JWT_SECRET_KEY = config.SECRET_KEY
        self.config.JWT_ACCESS_COOKIE_NAME = config.COOKIE_NAME
        self.config.JWT_TOKEN_LOCATION = ['cookies']

        self.security = AuthX(config=self.config)

    def get_token(self, uid: str, info=None):
        return self.security.create_access_token(uid=uid, data=info)

    def set_token(self, response,uid: str, info=None):
        token = self.security.create_access_token(uid=uid, data=info)

        response.set_cookie(
            key=self.config.JWT_ACCESS_COOKIE_NAME,
            value=token,
            httponly=True,
            max_age=3600,
            path="/",
            samesite="lax",
            secure=False
        )

    def get_security(self):
        return self.security

    def get_cookie_name(self):
        return self.config.JWT_ACCESS_COOKIE_NAME



