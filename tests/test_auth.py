def test_register(client):
    response = client.post("/api/v1/auth/register", json={
        "full_name": "Test User",
        "email": "testuser@example.com",
        "password": "Test123!"
    })

    assert response.status_code in [200, 400]