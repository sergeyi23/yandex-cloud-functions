import string
from dataclasses import dataclass


@dataclass
class LoginRequest:
    user_name: string
    password: string