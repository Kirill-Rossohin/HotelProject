from src.hotelproject.database.database import get_connection
from src.hotelproject.models.hotel import Hotel


def create(name: str, owner_id: int):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO hotels(name, owner_id)
        VALUES (?, ?)
    """, (name, owner_id))

    conn.commit()
    conn.close()


def get_by_id(hotel_id: int) -> Hotel | None:
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT hotel_id, name, owner_id
        FROM hotels
        WHERE hotel_id = ?
    """, (hotel_id,))

    row = cur.fetchone()
    conn.close()

    if not row:
        return None

    return Hotel(*row)


def get_by_owner_id(owner_id: int) -> Hotel | None:
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT hotel_id, name, owner_id
        FROM hotels
        WHERE owner_id = ?
    """, (owner_id,))

    row = cur.fetchone()
    conn.close()

    if not row:
        return None

    return Hotel(*row)


def get_by_name(name: str) -> Hotel | None:
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT hotel_id, name, owner_id
        FROM hotels
        WHERE name = ?
    """, (name,))

    row = cur.fetchone()
    conn.close()

    if not row:
        return None

    return Hotel(*row)


def get_all() -> list[Hotel]:
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT hotel_id, name, owner_id
        FROM hotels
        ORDER BY name
    """)

    rows = cur.fetchall()
    conn.close()

    return [Hotel(*row) for row in rows]


def delete(hotel_id: int):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        DELETE FROM hotels
        WHERE hotel_id = ?
    """, (hotel_id,))

    conn.commit()
    conn.close()