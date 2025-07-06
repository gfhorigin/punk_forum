from fastapi.testclient import TestClient
from main import app, tm


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


def test_login_cookie():
    client = TestClient(app)
    login_resp = client.post("/login", json={"email": "admin", "password": "admin"})
    assert login_resp.cookies.get(tm.get_cookie_name()) is not None


def test_login_cookie_failed():
    client = TestClient(app)
    login_resp = client.post("/login", json={"email": "admin", "password": "odmin"})
    assert login_resp.cookies.get(tm.get_cookie_name()) is None


def test_registration_cookie():
    client = TestClient(app)
    reg_resp = client.post("/registration", json={"email": "odmin", "password": "admin"})
    assert reg_resp.cookies.get(tm.get_cookie_name()) is not None


def test_registration_cookie_failed():
    client = TestClient(app)
    reg_resp = client.post("/registration", json={"email": "admin", "password": "admin"})
    assert reg_resp.cookies.get(tm.get_cookie_name()) is None


def test_check_auth():
    client = TestClient(app)
    client.post("/login", json={"email": "admin", "password": "admin"})
    auth = client.get("/check-auth")
    assert auth.status_code == 200


def test_check_auth_failed():
    client = TestClient(app)
    auth = client.get("/check-auth")
    assert auth.status_code == 403
