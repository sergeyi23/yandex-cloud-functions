from dataclasses import dataclass


@dataclass
class User:
    user_name: str
    password_hash: str
    password_salt: str

    def verify_password(self, password: str) -> bool:
        # Dummy response
        return True