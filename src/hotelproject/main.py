from src.hotelproject.database.database import init_db

from src.hotelproject.auth import (
    login,
    register,
    register_admin_ui
)

from src.hotelproject.menu import admin_menu, client_menu

from src.hotelproject.services.auth_service import create_default_admin


def main():
    init_db()
    create_default_admin()

    while True:
        print("\nОтель")
        print("1. Вход")
        print("2. Регистрация пользователя")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            user = login()

            if not user:
                continue

            if user.user_role == 2:
                admin_menu(user)
            else:
                client_menu(user)

        elif choice == "2":
            register()

        elif choice == "0":
            print("До свидания!")
            break

        else:
            print("Неверный выбор")


if __name__ == "__main__":
    main()