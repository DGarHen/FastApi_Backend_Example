from fastapi import status
from models import Customer, CustomerPlan, StatusEnum

testUser = {"name": "Jhon Doe", "description":"test user", "email": "jd@email.com", "age": 40}

def test_create_new_customer(client):
    response = client.post("/customers", json=testUser)
    assert response.status_code == status.HTTP_201_CREATED

def test_get_customer(client):
    response = client.post("/customers", json=testUser)
    assert response.status_code == status.HTTP_201_CREATED

    customer_id = response.json()["id"]
    response2 = client.get(f"/customers/{customer_id}")
    assert response2.status_code == status.HTTP_200_OK
    assert response2.json()["name"] == testUser["name"]
