from fastapi.testclient import TestClient

def testClient(client):
    assert type(client) == TestClient