from dataclasses import dataclass
@dataclass
class Reservation:
    reservation_id: int
    user_id: int
    room_id: int
    reserved_at: str
    reservation_end: str
    status: bool
    status_name: str | None = None