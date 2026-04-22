from app.db.session import SessionLocal
from app.models.user import User

def get_admin_token(client):
    # Creates admin directly
    client.post("/api/v1/auth/register", json={
        "full_name": "Admin User",
        "email": "admin@bankprotect.com",
        "password": "Admin123!",
        "role": "admin"   #
    })

    # Login
    response = client.post("/api/v1/auth/login", json={
        "email": "admin@bankprotect.com",
        "password": "Admin123!"
    })

    assert response.status_code == 200
    return response.json()["access_token"]

def get_user_token(client):
    client.post("/api/v1/auth/register", json={
        "full_name": "Test User",
        "email": "testuser@example.com",
        "password": "Test123!"
    })

    response = client.post("/api/v1/auth/login", json={
        "email": "testuser@example.com",
        "password": "Test123!"
    })

    return response.json()["access_token"]

#   VIEW USERS
def test_admin_get_users(client):
    token = get_admin_token(client)

    response = client.get(
        "/api/v1/admin/users",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
    assert "data" in response.json()


# NORMAL USER CANNOT ACCESS ADMIN
def test_user_cannot_access_admin(client):
    token = get_user_token(client)

    response = client.get(
        "/api/v1/admin/users",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 403


#  ADMIN CAN GET SINGLE USER
def test_admin_get_single_user(client):
    token = get_admin_token(client)

    # Create a user first
    client.post("/api/v1/auth/register", json={
        "full_name": "Test User",
        "email": "user2@example.com",
        "password": "Test123!"
    })

    # Get all users = extract real ID
    users = client.get(
        "/api/v1/admin/users",
        headers={"Authorization": f"Bearer {token}"}
    ).json()

    employee_id = users["data"][0]["employee_id"]

    response = client.get(
        f"/api/v1/admin/users/{employee_id}",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200


#  ADMIN CAN DEACTIVATE USER
def test_admin_deactivate_user(client):
    token = get_admin_token(client)

    client.post("/api/v1/auth/register", json={
        "full_name": "Test User",
        "email": "user3@example.com",
        "password": "Test123!"
    })

    users = client.get(
        "/api/v1/admin/users",
        headers={"Authorization": f"Bearer {token}"}
    ).json()

    employee_id = users["data"][0]["employee_id"]

    response = client.patch(
        f"/api/v1/admin/users/{employee_id}/deactivate",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200