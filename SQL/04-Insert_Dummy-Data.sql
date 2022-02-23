-- INSERT INTO tags (name)
-- VALUES ("Video Games"), ("Bootcamp"),("Corporative"),("Food");

-- INSERT INTO cities (name)
-- VALUES ("São Paulo"), ("Bauru"),("Campinas"),("Sorocaba");

-- INSERT INTO locations(title,street,house_number,postal_code,city_name)
-- VALUES ('CamposElisios', "Rua fernando cacheias","198A","17212-568","São Paulo");

-- INSERT INTO users (first_name, last_name,birthdate,email)
-- VALUES ('João','Silva','1998-08-19','joão@email.com');

-- INSERT INTO organizers (password,users_id)
-- VALUES ("b12sQ1@@",1); -- the program does the ENCRYPTION on the DATABASE

INSERT INTO events(name,date_planned,image,description,max_participants,min_age,locations_id,organizers_id)
VALUES(
    "Gamer Developer Bootcamp",
    "2022-10-19",
    "path/to/GameDev.jpg",
    "Venha aprender as habilidades principais dum criador de jogos!",
    100,
    16,
    1,
    1
);