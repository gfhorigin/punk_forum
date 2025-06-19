from fastapi.responses import JSONResponse


def success_response(message: str = "successfully", data: dict = None):
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
def invalid_credentials():
    return error_response(401, "invalid_credentials", "Неверный логин или пароль")


def email_exists():
    return error_response(400, "invalid_email", "Этот пользователь уже есть")
