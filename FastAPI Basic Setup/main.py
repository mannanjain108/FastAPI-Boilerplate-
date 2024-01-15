import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.v1.api import router


from helpers.get_env_vars import get_settings

env_vars = get_settings()

app = FastAPI(
    title=env_vars.app_name,
    version=env_vars.version,
    docs_url="/backend/api/v1/docs",
    redoc_url="/backend/api/v1/redoc",
    openapi_url="/backend/api/v1/openapi.json",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/backend/api/v1")

if __name__ == "__main__":
    uvicorn.run(
        app="main:app", host="127.0.0.1", port=8000, reload=not env_vars.is_prod
    )
