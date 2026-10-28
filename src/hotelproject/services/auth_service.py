import hashlib
from src.hotelproject.repositories import user_repository
from src.hotelproject.models.user import User


CLIENT_ROLE_ID = 1
ADMIN_ROLE_ID = 2

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


def authenticate(login: str, password: str) -> User | None:
    user = user_repository.get_by_login(login)

    if not user:
        return None

    if user.password_hash != hash_password(password):
        return None

    return user


def register_user(
    name: str,
    surname: str,
    patronymic: str | None,
    login: str,
    password: str
):
    if user_repository.get_by_login(login):
        raise Exception("Пользователь уже существует")

    user_repository.create(
        name=name,
        surname=surname,
        patronymic=patronymic,
        login=login,
        password_hash=hash_password(password),
        user_role=CLIENT_ROLE_ID
    )


def register_admin(
    name: str,
    surname: str,
    patronymic: str | None,
    login: str,
    password: str
):
    if user_repository.get_by_login(login):
        raise Exception("Пользователь уже существует")

    user_repository.create(
        name=name,
        surname=surname,
        patronymic=patronymic,
        login=login,
        password_hash=hash_password(password),
        user_role=ADMIN_ROLE_ID
    )


def create_default_admin():
    if user_repository.get_by_login("admin"):
        return

    user_repository.create(
        name="System",
        surname="Admin",
        patronymic=None,
        login="admin",
        password_hash=hash_password("admin"),
        user_role=ADMIN_ROLE_ID
    )