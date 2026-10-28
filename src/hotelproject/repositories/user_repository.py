from src.hotelproject.database.database import get_connection
from src.hotelproject.models.user import User


def _map(row) -> User:
    return User(*row)


def create(
    name: str, 
    surname: str, 
    patronymic: str | None, 
    login: str, 
    password_hash: str, 
    user_role: str
):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO users(name, surname, patronymic, login, password_hash, user_role)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (name, surname, patronymic, login, password_hash, user_role))

    conn.commit()
    conn.close()


def get_by_login(login: str) -> User | None:
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT user_id, name, surname, patronymic, login, password_hash, user_role
        FROM users
        WHERE login = ?
    """, (login,))

    row = cur.fetchone()
    conn.close()

    return _map(row) if row else None


def get_by_id(user_id: int) -> User | None:
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT user_id, name, surname, patronymic, login, password_hash, user_role
        FROM users
        WHERE user_id = ?
    """, (user_id,))

    row = cur.fetchone()
    conn.close()

    return _map(row) if row else None


def get_all() -> list[User]:
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT user_id, name, surname, patronymic, login, password_hash, user_role
        FROM users
        ORDER BY surname, name
    """)

    rows = cur.fetchall()
    conn.close()

    return [_map(r) for r in rows]