from src.hotelproject.repositories import hotel_repository
from src.hotelproject.models.hotel import Hotel


def create_hotel(name: str, owner_id: int):

    if not name.strip():
        raise Exception("Имя не может быть пустым")

    hotels = hotel_repository.get_all()

    for i in hotels:
        if i.name.lower() == name.lower():
            raise Exception("Имя гостиницы занято")

    hotel_repository.create(name, owner_id)


def get_all_hotels() -> list[Hotel]:
    return hotel_repository.get_all()


def get_hotel_by_id(hotel_id: int) -> Hotel | None:
    return hotel_repository.get_by_id(hotel_id)


def delete_hotel(hotel_id: int):
    hotel = hotel_repository.get_by_id(hotel_id)

    if not hotel:
        raise Exception("Отель не найден")

    hotel_repository.delete(hotel_id)