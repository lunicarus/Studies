create TABLE events (
    id SERIAL PRIMARY KEY,
    name VARCHAR(300) NOT NULL CHECK (LENGTH(name) > 5),
    date_planned TIMESTAMP NOT NULL,
    image VARCHAR(500),
    description TEXT NOT NULL,
    max_participants INT CHECK (max_participants > 0),
    min_age INT CHECK (min_age > 0)
);