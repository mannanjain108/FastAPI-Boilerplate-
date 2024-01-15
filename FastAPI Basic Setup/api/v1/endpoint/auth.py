from http import HTTPStatus
from fastapi import APIRouter

from helpers import response_parser
from constants import messages

auth_router = APIRouter(prefix="/auth")


@auth_router.get("/")
def index():
    try:
        return response_parser.generate_response(message=messages.SUCCESSFULL_SETUP)
    except Exception as err:
        if hasattr(err, "status_code"):
            raise err
        raise response_parser.generate_response(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            message=messages.INTERNAL_SERVER_ERROR,
        )
