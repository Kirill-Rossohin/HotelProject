import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
from src.hotelproject.repositories import reservation_repository, hotel_repository, room_repository
from src.hotelproject.models.room import Room


def create_room(hotel_id: int, capacity: int):
    hotel = hotel_repository.get_by_id(hotel_id)
    if not hotel:
        raise Exception("Отель не найден")
    if capacity <= 0:
        raise Exception("Вместимость комнаты должна быть больше 0")
    room_repository.create(hotel_id, capacity)

def update_room(room_id: int, capacity: int):
    if capacity <= 0:
        raise Exception("Вместимость комнаты должна быть больше нуля")
    room_repository.update_capacity(room_id, capacity)

def get_all_rooms_of_a_hotel(hotel_id: int) -> list[Room]:
    return room_repository.get_all_hotels_rooms(hotel_id)


def get_room_by_id(room_id: int) -> Room | None:
    return room_repository.get_by_id(room_id)


def delete_room(room_id: int):

    if not room_repository.get_by_id(room_id):
        raise Exception("Комната не найдена")
    room_repository.delete(room_id)


def is_room_available(room_id: int) -> bool:
    room = room_repository.get_by_id(room_id)
    if room is None:
        return False
    active_reservations = reservation_repository.get_active_by_room(room_id)
    occupied_places = len(active_reservations)
    return occupied_places < room.capacity