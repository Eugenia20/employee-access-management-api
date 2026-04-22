# Identity Access Management API

Production-ready backend system built with FastAPI, implementing secure authentication and role-based access control (RBAC).

## Features
- JWT Authentication
- Role-Based Access Control (Admin/User)
- User lifecycle management
- PostgreSQL + SQLAlchemy
- Alembic migrations
- Pytest test coverage
- Dockerized setup

## Run locally
```bash
uvicorn app.main:app --reload