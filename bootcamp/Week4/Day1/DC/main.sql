-- Instructions
-- In this exercise we will be using the actors table from todays lesson.
-- 1. Count how many actors are in the table.
-- 2. Try to add a new actor with some blank fields. What do you think the outcome will be ?
SELECT COUNT(*) FROM actors;
INSERT INTO actors (first_name, last_name) VALUES ('Joe', 'Posel');

