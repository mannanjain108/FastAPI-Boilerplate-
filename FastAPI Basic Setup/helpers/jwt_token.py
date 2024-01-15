from datetime import datetime, timedelta
from jose import JWTError, jwt

from helpers import get_env_vars

env_vars = get_env_vars.get_settings()


def create_access_token(
    data: dict, expire_time: int = env_vars.auth_jwt_expire_validity
):
    try:
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=expire_time)
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, env_vars.secret_key, env_vars.algorithm)
    except Exception as err:
        print(err)


# def get_current_user()
