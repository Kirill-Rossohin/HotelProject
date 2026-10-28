from src.hotelproject.auth import register_admin_ui

from src.hotelproject.services.hotel_service import (
    create_hotel,
    get_all_hotels,
    delete_hotel,
    get_hotel_by_owner_id
)

from src.hotelproject.services.room_service import (
    create_room,
    get_all_rooms,
    delete_room,
    get_all_rooms_of_a_hotel,
    get_room_by_id
)

from src.hotelproject.services.reservation_service import (
    create_reservation,
    get_user_reservations,
    get_all_reservations,
    cancel_reservation
)


# -------------------------
# ADMIN MENU
# -------------------------
def admin_menu(user):

    while True:

        print(f"\nАдминистратор ({user.login})")
        print("1. Меню гостиницы")
        print("2. Меню бронирований")
        print("3. Добавить администратора")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            hotel_menu(user)

        elif choice == "2":
            reservations_menu(user)

        elif choice == "3":
            register_admin_ui(user)

        elif choice == "0":
            break


# -------------------------
# CLIENT MENU
# -------------------------
def client_menu(user):

    while True:

        print(f"\nЧитатель ({user.login})")
        print("1. Список гостиниц")
        print("2. Мои брони")
        print("3. Забронировать комнату")
        print("4. Список комнат")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":

            hotels = get_all_hotels()

            if not hotels:
                print("\nГостиниц нет")
                continue

            for i in hotels:
                print(f"{i}. {i.name}")

        elif choice == "2":

            reservations = get_user_reservations(user.user_id)

            if not reservations:
                print("\nУ вас нет бронирований")
                continue

            for i in reservations:
                print(f"{i.reservation_id} | Room {i.room_id} | Status {i.status}")

        elif choice == "3":

            room_id = input("ID комнаты: ")

            try:
                create_reservation(user.user_id, int(room_id))
                print("Забронировано")
            except Exception as e:
                print(e)

        elif choice == "0":
            break
        elif choice == "4":
            rooms = get_all_rooms()
            for i in rooms:
                print(f'{i}')


# -------------------------
# HOTEL
# -------------------------
def hotel_menu(user):

    while True:

        print("\nГостиница")
        print("1. Добавить комнату")
        print("2. Редактировать комнаты")
        print("3. Удалить комнату")
        print("0. Назад")

        choice = input("Выберите: ")
        hotel = get_hotel_by_owner_id(user.user_id).hotel_id
        if choice == "1":

            create_room(
                hotel,
                int(input("Вместительность: "))
            )

            print("Комната добавлена")

        elif choice == "2":

            rooms = get_all_rooms_of_a_hotel(hotel)

            if not rooms:
                print("Нет комнат")
                continue

            print("\nСписок комнат:")

            for i in rooms:
                print(i)

            room = get_room_by_id(int(input("Введите ID нужной комнаты: ")))
            room.capacity = int(input("Введите новую вместительность: "))

        elif choice == "3":

            delete_room(int(input("Введите ID удаляемой комнаты: ")))
            print("Комната удалена")

        elif choice == "0":
            break



# -------------------------
# RESERVATIONS
# -------------------------
def reservations_menu(user):

    while True:

        print("\nБронирования")
        print("1. Все")
        print("2. Отменить чью-то бронь")
        print("0. Назад")

        choice = input("Выберите: ")

        if choice == "1":

            reservations = get_all_reservations()

            if not reservations:
                print("Нет бронирований")
                continue

            for r in reservations:
                print(f"{r.reservation_id} | Room {r.room_id} | Status {r.status}")

        elif choice == "2":

            reservation_id = input("ID брони: ")

            try:
                cancel_reservation(int(reservation_id), user.user_id, user.user_role)
                print("Отменено")
            except Exception as e:
                print(e)

        elif choice == "0":
            break