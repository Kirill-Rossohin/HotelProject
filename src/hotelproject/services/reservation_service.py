from src.hotelproject.repositories import room_repository, reservation_repository, user_repository
from src.hotelproject.services import room_service
from src.hotelproject.models.reservation import Reservation


INACTIVE_STATUS_ID = 0
ACTIVE_STATUS_ID = 1

CLIENT_ROLE_ID = 1
ADMIN_ROLE_ID = 2


def create_reservation(user_id: int, room_id: int):

    user = user_repository.get_by_id(user_id)

    if not user or user.user_role != CLIENT_ROLE_ID:
        raise Exception("Только клиенты могут бронировать комнату")

    if not room_repository.get_by_id(room_id):
        raise Exception("Указанной комнаты не существует")

    if not room_service.is_room_available(room_id):
        raise Exception("В комнате нет свободного места")

    reservation_repository.create(user_id, room_id)


def get_all_reservations() -> list[Reservation]:
    return reservation_repository.get_all()


def get_user_reservations(user_id: int) -> list[Reservation]:
    return reservation_repository.get_by_user(user_id)


def cancel_reservation(reservation_id: int, user_id: int, user_role: int):

    reservation = reservation_repository.get_by_id(reservation_id)

    if not reservation:
        raise Exception("Бронь не найдена")

    if reservation.user_id != user_id and user_role == CLIENT_ROLE_ID:
        raise Exception("Нельзя отменить чужую бронь")

    if reservation.status != ACTIVE_STATUS_ID:
        raise Exception("Бронь уже закрыта")

    reservation_repository.cancel(reservation_id)