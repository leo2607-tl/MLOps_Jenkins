from fastapi.testclient import TestClient
from api_check import app

client = TestClient(app)

#test_file
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

if __name__ == "__main__":
    print("Running tests...")
    
    try:
        test_get_version()
        print("test_get_version passed")
        
        test_prime_1()
        print("test_prime_1 passed")
        
        test_prime_2()
        print("test_prime_2 passed")
        
        test_prime_3()
        print("test_prime_3 passed")
        
        test_prime_4()
        print("test_prime_4 passed")
        
        test_prime_29()
        print("test_prime_29 passed")
        
        test_prime_negative()
        print("test_prime_negative passed")
        
        test_prime_large()
        print("test_prime_large passed")
        
        test_prime_zero()
        print("test_prime_zero passed")
        
        test_prime_non_integer()
        print("test_prime_non_integer passed")
        
        print("All tests passed successfully!")
    except AssertionError as e:
        print(f"Test failed: {e}")
