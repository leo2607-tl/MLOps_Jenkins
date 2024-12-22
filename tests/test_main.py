import pytest
from fastapi.testclient import TestClient
from api_check import app

client = TestClient(app)

def test_get_version():
    response = client.get("/version")
    assert response.status_code == 200
    assert response.json() == {"version": "1.0.0"}

def test_prime_1():
    response = client.post("/check_prime", json={"value": 1})
    assert response.status_code == 200
    assert response.json() == {"is_prime": False}

def test_prime_2():
    response = client.post("/check_prime", json={"value": 2})
    assert response.status_code == 200
    assert response.json() == {"is_prime": True}

def test_prime_3():
    response = client.post("/check_prime", json={"value": 3})
    assert response.status_code == 200
    assert response.json() == {"is_prime": True}

def test_prime_4():
    response = client.post("/check_prime", json={"value": 4})
    assert response.status_code == 200
    assert response.json() == {"is_prime": False}

def test_prime_29():
    response = client.post("/check_prime", json={"value": 29})
    assert response.status_code == 200
    assert response.json() == {"is_prime": True}

def test_prime_negative():
    response = client.post("/check_prime", json={"value": -5})
    assert response.status_code == 200
    assert response.json() == {"is_prime": False}

def test_prime_large():
    response = client.post("/check_prime", json={"value": 997})
    assert response.status_code == 200
    assert response.json() == {"is_prime": True}

def test_prime_zero():
    response = client.post("/check_prime", json={"value": 0})
    assert response.status_code == 200
    assert response.json() == {"is_prime": False}

def test_prime_non_integer():
    response = client.post("/check_prime", json={"value": "abc"})
    assert response.status_code == 422
