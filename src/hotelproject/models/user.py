from dataclasses import dataclass
@dataclass
class User:
    user_id: int
    name: str
    surname: str
    patronymic: str | None
    login: str
    password_hash: str
    user_role: int
    role_name: str | None = None