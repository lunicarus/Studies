-- merge related data
-- SELECT 
-- e.id AS event_id,
-- e.name,
-- e.date_planned,
-- loc.title,
-- loc.street,
-- loc.house_number,
-- loc.city_name,
-- u.first_name,
-- u.email
--     FROM events AS e
-- INNER JOIN locations AS loc ON  e.locations_id = loc.id
-- INNER JOIN events_user AS eu ON eu.events_id = e.id
-- INNER JOIN users AS u ON eu.users_id = u.id;

-- left join gives all data from the left(events) and the related data ON the condition defined,
-- SELECT * FROM locations as loc
-- LEFT JOIN events as e ON  e.locations_id = loc.id; 