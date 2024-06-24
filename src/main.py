from fastapi import FastAPI
from fastapi_users import FastAPIUsers

from src.auth.auth_backend import auth_backend
from src.auth.manager import get_user_manager
from src.auth.schemas import UserRead, UserCreate
from src.db.models import User

app = FastAPI(
    title="Scheduler API"
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)