import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass
class DBConfig:
    host:       str = os.environ.get("DB_HOST")
    port:       int = os.environ.get("DB_PORT")
    name:       str = os.environ.get("DB_NAME")
    user:       str = os.environ.get("DB_USER")
    password:   str = os.environ.get("DB_PASSWORD")
    echo:       bool = True

    @property
    def full_url(self) -> str:
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"
