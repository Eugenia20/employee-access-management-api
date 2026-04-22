def test_get_me(client):
    # creating user first
    client.post("/api/v1/auth/register", json={
        "full_name": "Test User",
        "email": "testuser@example.com",
        "password": "Test123!"
    })

    login = client.post("/api/v1/auth/login", json={
        "email": "testuser@example.com",
        "password": "Test123!"
    })

    token = login.json()["access_token"]

    response = client.get(
        "/api/v1/users/me",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200