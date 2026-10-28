from src.hotelproject.database.database import get_connection
from src.hotelproject.models.reservation import Reservation


def _map(row) -> Reservation:
    return Reservation(*row)


def create(user_id: int, room_id: int):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO reservations(
            user_id,
            room_id,
            reserved_at,
            reservation_end,
            status
        )
        VALUES (?, ?, datetime('now'), datetime('now', '+7 days'), 1)
    """, (user_id, room_id))

    conn.commit()
    conn.close()


def get_by_id(reservation_id: int) -> Reservation | None:
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT reservation_id, user_id, room_id, reserved_at, reservation_end, status
        FROM reservations
        WHERE reservation_id = ?
    """, (reservation_id,))

    row = cur.fetchone()
    conn.close()

    return _map(row) if row else None


def get_all() -> list[Reservation]:
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT reservation_id, user_id, room_id, reserved_at, reservation_end, status
        FROM reservations
        ORDER BY reserved_at DESC
    """)

    rows = cur.fetchall()
    conn.close()

    return [_map(r) for r in rows]


def get_by_user(user_id: int) -> list[Reservation]:
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT reservation_id, user_id, room_id, reserved_at, reservation_end, status
        FROM reservations
        WHERE user_id = ?
        ORDER BY reserved_at DESC
    """, (user_id,))

    rows = cur.fetchall()
    conn.close()

    return [_map(r) for r in rows]


def get_active_by_room(room_id: int) -> Reservation | None:
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT reservation_id, user_id, room_id, reserved_at, reservation_end, status
        FROM reservations
        WHERE room_id = ? AND status = 1
    """, (room_id,))

    row = cur.fetchone()
    conn.close()

    return _map(row) if row else None


def mark_returned(reservation_end: str, reservation_id: int):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        UPDATE reservations
        SET reservation_end = ?
        WHERE reservation_id = ?
    """, (reservation_end, reservation_id))

    conn.commit()
    conn.close()


def cancel(reservation_id: int):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        UPDATE reservations
        SET status = 0,
        reservation_end = datetime('now')
        WHERE reservation_id = ?
    """, (reservation_id,))

    conn.commit()
    conn.close()