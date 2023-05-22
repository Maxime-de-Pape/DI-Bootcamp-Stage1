-- 🌟 Exercise 1 : Items And Customers
-- Instructions
-- We will work on the public database that we created yesterday.
--
-- Use SQL to get the following from the database:
-- All items, ordered by price (lowest to highest).
-- Items with a price above 80 (80 included), ordered by price (highest to lowest).
-- The first 3 customers in alphabetical order of the first name (A-Z) – exclude the primary key column from the results.
-- All last names (no other columns!), in reverse alphabetical order (Z-A)

SELECT * FROM items
ORDER BY price DESC;

SELECT * FROM items
WHERE price <= 80
ORDER BY price ASC

SELECT first_name, last_name FROM customers
ORDER BY first_name DESC
LIMIT 3

SELECT first_name FROM customers
ORDER BY last_name ASC





