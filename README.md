# Employee Access Management API

A production-ready FastAPI backend for managing employees, authentication, and role-based access control.

## 🚀 Features

* JWT Authentication
* Role-based access control (Admin/User)
* User activation/deactivation
* PostgreSQL database
* Dockerized environment
* Automated testing with Pytest

## 🐳 Run with Docker

```bash
docker-compose up --build
```

API will be available at:

http://localhost:8002

Swagger Docs:

http://localhost:8002/docs

## 🧪 Run Tests

```bash
pytest
```

## 🛠 Tech Stack

* FastAPI
* PostgreSQL
* SQLAlchemy
* Docker
* Pytest
* JWT (python-jose)

## 📌 Notes

* Admin endpoints are protected
* Default role: user
* Admin role required for management routes
