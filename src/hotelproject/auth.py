from src.hotelproject.services.auth_service import (
    authenticate,
    register_user,
    register_admin,
    create_default_admin
)


def login():
    print("\nАвторизация")

    login_value = input("Логин: ")
    password_value = input("Пароль: ")

    user = authenticate(login_value, password_value)

    if not user:
        print("\nНеверный логин или пароль")
        return None

    print(f"\nДобро пожаловать, {user.name} {user.surname}")
    return user


def register():
    print("\nРегистрация клиента")

    name = input("Имя: ")
    surname = input("Фамилия: ")
    patronymic = input("Отчество: ")

    login_value = input("Логин: ")
    password_value = input("Пароль: ")

    try:
        register_user(name, surname, patronymic, login_value, password_value)
        print("\nРегистрация успешна")
    except Exception as e:
        print(f"\nОшибка: {e}")


def register_admin_ui():
    print("\nРегистрация администратора")

    name = input("Имя: ")
    surname = input("Фамилия: ")
    patronymic = input("Отчество: ")

    login_value = input("Логин: ")
    password_value = input("Пароль: ")

    try:
        register_user(name, surname, patronymic, login_value, password_value)
        print("\nАдминистратор создан")
    except Exception as e:
        print(f"\nОшибка: {e}")