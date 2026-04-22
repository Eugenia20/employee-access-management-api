import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    def __init__(self):
        self.DATABASE_URL = os.getenv("DATABASE_URL")
        self.SECRET_KEY = os.getenv("SECRET_KEY")
        self.ALGORITHM = os.getenv("ALGORITHM")
        self.ACCESS_TOKEN_EXPIRE_MINUTES = int(
            os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30)
        )

settings = Settings()