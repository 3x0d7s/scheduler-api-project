from fastapi import FastAPI, Depends

from src.auth.config import auth_backend, fastapi_users
from src.auth.schemas import UserRead, UserCreate

from src.schedules.routers import router as schedules_router
from src.events.routers import router as events_router
from src.subscriptions.routers import router as subscriptions_router

from src.auth.models import User
from src.events.models import Event
from src.subscriptions.models import Subscription
from src.schedules.models import Schedule

app = FastAPI(
    title="Scheduler API"
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

app.include_router(schedules_router)
app.include_router(events_router)
app.include_router(subscriptions_router)

current_user = fastapi_users.current_user()


@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.email}"
