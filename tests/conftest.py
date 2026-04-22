import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.db.session import Base
from app.api.v1.deps import get_db
from fastapi.testclient import TestClient

# TEST DATABASE(only for testing)
TEST_DATABASE_URL = "postgresql+psycopg2://postgres:Ibimina_08@localhost:5432/employee_test"

engine = create_engine(TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


#Override dependency
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(scope="function")
def client():
    # 🧹 Create tables fresh for each test
    Base.metadata.create_all(bind=engine)

    yield TestClient(app)

    # 🧹 Clean DB after test
    Base.metadata.drop_all(bind=engine)