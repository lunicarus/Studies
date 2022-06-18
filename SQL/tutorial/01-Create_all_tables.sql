CREATE DATABASE LZeventos;

CREATE TABLE cities(
    name VARCHAR(200) PRIMARY KEY
);
CREATE TABLE locations (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(200),
    street VARCHAR(200) NOT NULL,
    house_number VARCHAR(10) NOT NULL,
    postal_code VARCHAR(10) NOT NULL,
    city_name VARCHAR(200) REFERENCES cities ON DELETE RESTRICT
);
CREATE TABLE users(
    id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(150) NOT NULL,
    last_name VARCHAR(150) NOT NULL,
    birthdate DATE NOT NULL,
    email VARCHAR(100) NOT NULL
);

CREATE TABLE organizers(
    password VARCHAR(20),
    users_id INT PRIMARY KEY REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE tags(
    name VARCHAR(100) PRIMARY KEY 
);

CREATE TABLE events (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(300) NOT NULL CHECK (LENGTH(name) > 5),
    date_planned TIMESTAMP NOT NULL,
    image VARCHAR(500),
    description TEXT NOT NULL,
    max_participants INT CHECK (max_participants > 0),
    min_age INT CHECK (min_age > 0),
    locations_id INT REFERENCES locations ON DELETE CASCADE,
    organizers_id INT REFERENCES organizers ON DELETE CASCADE
);

CREATE TABLE events_user (
    events_id INT REFERENCES events ON DELETE CASCADE,
    users_id INT REFERENCES users ON DELETE CASCADE,
    PRIMARY KEY(events_id,users_id)
);

CREATE TABLE events_tags (
    events_id INT REFERENCES events ON DELETE CASCADE,
    tags_name VARCHAR(100) REFERENCES tags ON DELETE CASCADE,
    PRIMARY KEY(events_id,tags_name)
);