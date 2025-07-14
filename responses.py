from fastapi.responses import JSONResponse
import config


def success_response(message: str = config.SUCCESS_BASE, data: dict = None):
    return JSONResponse(
        status_code=200,
        content={
            "success": True,
            "error": None,
            "message": message,
            "data": data or {}
        }
    )


def error_response(
        status_code: int,
        error_type: str,
        message: str
):
    return JSONResponse(
        status_code=status_code,
        content={
            "success": False,
            "error": error_type,
            "message": message
        }
    )


# Конкретные ошибки
def invalid_auth():
    return error_response(403, config.INVALID_AUTH, config.M_INVALID_AUTH)


def invalid_credentials():
    return error_response(401, config.INVALID_CREDENTIALS, config.M_INVALID_CREDENTIALS)


def email_exists():
    return error_response(400, config.EMAIL_EXISTS, config.M_EMAIL_EXISTS)


def unique_exists():
    return error_response(400, config.EMAIL_EXISTS, config.M_EMAIL_UNIQUE)