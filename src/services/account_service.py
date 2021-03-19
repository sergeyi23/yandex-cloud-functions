from src.database import user_repository
from src.models.login_request import LoginRequest
from src.models.login_response import LoginResponse


def login(login_request: LoginRequest):
    # do business logic here
    user = user_repository.get_user(login_request.user_name)
    if user is None:
        LoginResponse(False)
    is_valid_password = user.verify_password(login_request.password)
    return LoginResponse(is_valid_password)

def signup():
    raise NotImplemented()