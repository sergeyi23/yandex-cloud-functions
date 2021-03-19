from dataclasses import dataclass


@dataclass
class LoginResponse:
    success: bool = False
