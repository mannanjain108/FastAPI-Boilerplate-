from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException

from schemas import api_response


def generate_response(
    status_code=200,
    message="",
    data=[],
    success=True,
    media_type="application/json",
    headers={},
):
    try:
        if status_code not in [200, 201, 202, 204]:
            return HTTPException(
                status_code=status_code,
                detail=jsonable_encoder(
                    api_response.APIResponse(
                        status_code=status_code,
                        message=str(message),
                        data=data,
                        success=success,
                    ).model_dump()
                ),
            )
        else:
            return JSONResponse(
                status_code=status_code,
                media_type=media_type,
                headers=headers,
                content=jsonable_encoder(
                    api_response.APIResponse(
                        status_code=status_code,
                        message=str(message),
                        data=data,
                        success=success,
                    ).model_dump()
                ),
            )
    except Exception as err:
        print(err)
