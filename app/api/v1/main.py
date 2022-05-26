from fastapi import FastAPI
from app.api.v1.user.user_module import router as user_router

app = FastAPI(
    title="User API",
    description="User API",
    version="1.0.0",
    openapi_url="/api/v1/openapi.json",
    docs_url="/api/v1/docs",
    redoc_url="/api/v1/redoc",
)


app.include_router(user_router, prefix="/api/v1/user", tags=["user"])