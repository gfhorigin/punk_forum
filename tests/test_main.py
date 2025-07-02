import pytest
from httpx import AsyncClient, ASGITransport
from fastapi.testclient import TestClient

from main import app


def test_login():
    client = TestClient(app)
    response = client.post("/login", json={"email": "admin", "password": "admin"})
    assert response.status_code == 200


def test_login_wrong():
    client = TestClient(app)
    response = client.post("/login", json={"email": "odmin", "password": "admin"})
    assert response.status_code == 401
    response = client.post("/login", json={"email": "admin", "password": "odmin"})
    assert response.status_code == 401


def test_registration():
    client = TestClient(app)
    response = client.post("/registration", json={"email": "new_user", "password": "admin"})
    assert response.status_code == 200


def test_registration_wrong():
    client = TestClient(app)
    response = client.post("/registration", json={"email": "admin", "password": "admin"})
    assert response.status_code == 400


# -------------------------в будущих версиря будет удалено
# @pytest.mark.asyncio
# async def test_login():
#     async with AsyncClient(
#             transport=ASGITransport(app=app),
#             base_url="http://test",
#             cookies=None,
#             follow_redirects=True
#     ) as ac:
#         login_resp = await ac.post("/login", json={"email": "admin", "password": "admin"})
#         assert login_resp.status_code == 200
#         print(login_resp.cookies.get("token"))
#         print(ac.cookies)
#         # Проверка авторизации с куками
#         check_resp = await ac.get(
#             "/check-auth",
#             cookies=ac.cookies  # Критически важно!
#         )
#         assert check_resp.status_code == 200
#         print(check_resp.json())