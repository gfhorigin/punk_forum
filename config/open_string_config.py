# names
COOKIE_NAME = "token"
TABLE_USERS = "users"

# error types
INVALID_AUTH = "cookie not allowed"
INVALID_CREDENTIALS = "invalid_credentials"
EMAIL_EXISTS = "invalid_email"

# response messages
SUCCESS_BASE = "successfully"

# messages
M_INVALID_AUTH = "пользователь не прошел аунтефикацию"
M_INVALID_CREDENTIALS = "неверынй логин или пароль"
M_EMAIL_EXISTS = "такой пользователь уже существует"
M_EMAIL_UNIQUE = "данное имя уже занято"

# DOCK
documentation = "/registration - принимает nickname, unique_name, email, password в body post запроса" \
                "возвращет ошибку 401 в случае, если email или unique_name уже заняты или " \
                "возвращет строку типа /user/{unique_name}\n" \
                "/login - принимает email и password в body post запроса возвращает ошибку 401, в случае, если " \
                "невреное email или password или возвращет строку типа типа /user/{unique_name}\n" \
                "/check-auth - считывает куки и возвращает 403 в случае их отстутсвтия или данные о пользователе в " \
                "случае успеха "
