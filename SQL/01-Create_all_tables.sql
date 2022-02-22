CREATE TABLE cities(
    name VARCHAR(200) PRIMARY KEY
)

CREATE TABLE locations (
    id SERIAL PRIMARY KEY,
    title VARCHAR(200),
    street VARCHAR(200) NOT NULL CHECK (LENGTH(name) > 5,
    house_number VARCHAR(10) NOT NULL CHECK (LENGTH(name) > 0,
    postal_code VARCHAR(10) NOT NULL CHECK(LENGTH(name) > 3,
    city_name VARCHAR(200) REFERENCES cities ON DELETE RESTRICT ON UPDATE CASCADE
);
CREATE TABLE events (
    id SERIAL PRIMARY KEY,
    name VARCHAR(300) NOT NULL CHECK (LENGTH(name) > 5),
    date_planned TIMESTAMP NOT NULL,
    image VARCHAR(500),
    description TEXT NOT NULL,
    max_participants INT CHECK (max_participants > 0),
    min_age INT CHECK (min_age > 0),
    location_id INT REFERENCES locations ON DELETE CASCADE
    tags_id VARCHAR(100) REFERENCES tags ON DELETE CASCADE
);
CREATE TABLE tags(
    name VARCHAR(100) PRIMARY KEY 
)
CREATE users(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(150) NOT NULL,
    last_name VARCHAR(150) NOT NULL,
    birthdate DATE NOT NULL CHECK (birthdate < '30-12-2022'),
    email VARCHAR(100)
    organizers_password REFERENCES organizers ON DELETE CASCADE
)
CREATE organizers(
    password VARCHAR(20) PRIMARY KEY
)