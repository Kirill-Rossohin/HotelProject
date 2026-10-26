from dataclasses import dataclass
@dataclass
class Room:
    room_id: int
    hotel_id: int
    capacity: int