import os
from dotenv import load_dotenv

load_dotenv(override=False)

class Settings:
    def __init__(self):
        self.DATABASE_URL = os.getenv(
            "DATABASE_URL",
            "postgresql://postgres:postgres@localhost:5432/employee_test"
        )

        self.SECRET_KEY = os.getenv("SECRET_KEY", "testsecret123")
        self.ALGORITHM = os.getenv("ALGORITHM", "HS256")

        self.ACCESS_TOKEN_EXPIRE_MINUTES = int(
            os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30)
        )

settings = Settings()