from src.hotelproject.database.database import get_connection
from src.hotelproject.models.room import Room


def create(hotel_id: int, capacity: int):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO rooms(hotel_id, capacity)
        VALUES (?, ?)
    """, (hotel_id, capacity))

    conn.commit()
    conn.close()


def get_by_id(room_id: int) -> Room | None:
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT room_id, hotel_id, capacity
        FROM rooms
        WHERE room_id = ?
    """, (room_id,))

    row = cur.fetchone()
    conn.close()

    if not row:
        return None

    return Room(*row)


def get_all() -> list[Room]:
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT room_id, hotel_id, capacity
        FROM rooms
        ORDER BY hotel_id
    """)

    rows = cur.fetchall()
    conn.close()

    return [Room(*row) for row in rows]


def get_all_hotels_rooms(hotel_id: int) -> list[Room]:
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT room_id, hotel_id, capacity
        FROM rooms
        WHERE hotel_id = ?
    """, (hotel_id,))

    rows = cur.fetchall()
    conn.close()

    return [Room(*row) for row in rows]


def delete(room_id: int):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        DELETE FROM rooms
        WHERE room_id = ?
    """, (room_id,))

    conn.commit()
    conn.close()