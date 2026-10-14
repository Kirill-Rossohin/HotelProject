DROP TABLE IF EXISTS reservations;
DROP TABLE IF EXISTS rooms;
DROP TABLE IF EXISTS hotels;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS user_roles;

CREATE TABLE user_roles (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    role_name TEXT NOT NULL UNIQUE
);

CREATE TABLE users (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    surname TEXT NOT NULL,
    patronymic TEXT,
    password_hash TEXT NOT NULL,
    user_role INTEGER NOT NULL,
    FOREIGN KEY (user_role) REFERENCES user_roles (ID)
);

CREATE TABLE hotels (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    hotel_name TEXT NOT NULL,
    owner_id INTEGER NOT NULL,
    FOREIGN KEY (owner_id) REFERENCES users (ID)
);

CREATE TABLE rooms (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    hotel_id INTEGER NOT NULL,
    room_capacity INTEGER NOT NULL,
    FOREIGN KEY (hotel_id) REFERENCES hotels (ID)
);

CREATE TABLE reservations (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    room_id INTEGER NOT NULL,
    reserved_at TEXT NOT NULL,
    reservation_end TEXT NOT NULL,
    status BOOLEAN NOT NULL,

    FOREIGN KEY (user_id) REFERENCES users (ID),
    FOREIGN KEY (room_id) REFERENCES rooms (ID)
);

INSERT INTO user_roles (role_name)
VALUES ('Customer'), ('Admin');