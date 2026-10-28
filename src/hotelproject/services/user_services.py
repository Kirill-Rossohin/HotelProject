from src.hotelproject.repositories import user_repository


def authenticate(login: str, password_hash: str):
    return user_repository.find_by_credentials(login, password_hash)