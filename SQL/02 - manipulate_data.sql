-- INSERT INTO events(
--     name,
--     date_planned,
--     description,
--     max_participants,
--     min_age)

--     VALUES
--     (
--         'Gamer Event',
--         '2022-04-19 13:30:00',
--         'Everything a Gamer would want!',
--         100,
--         12
--     );
UPDATE events 
SET min_age = 14
WHERE id = 1;