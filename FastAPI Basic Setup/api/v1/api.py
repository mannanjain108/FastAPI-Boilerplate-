from fastapi import APIRouter

from api.v1.endpoint import auth

router = APIRouter()

router.include_router(auth.auth_router, tags=["Authentication"])
