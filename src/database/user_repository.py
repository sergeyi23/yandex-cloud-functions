from typing import Optional

from src.entities.user import User


def get_user(user_name: str) -> Optional[User]:
    # TODO: load user from database
    return User("dummy", "dummy", "dummy")