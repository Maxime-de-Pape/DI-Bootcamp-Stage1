-- Create 2 tables : Customer and Customer profile. They have a One to One relationship.
--
-- A customer can have only one profile, and a profile belongs to only one customer
-- The Customer table should have the columns : id, first_name, last_name NOT NULL
-- The Customer profile table should have the columns : id, isLoggedIn DEFAULT false (a Boolean), customer_id (a reference to the Customer table)

-- CREATE TABLE CustomerProfile (
--   id SERIAL PRIMARY KEY,
--   isLoggedIn BOOLEAN DEFAULT false,
--   customer_id INT UNIQUE,
--   FOREIGN KEY (customer_id) REFERENCES Customer(id)

------------------------------------------------------------
--
-- CREATE TABLE CustomerProfile (
--   id SERIAL PRIMARY KEY,
--   isLoggedIn BOOLEAN DEFAULT false,
--   customer_id INT UNIQUE,
--   FOREIGN KEY (customer_id) REFERENCES Customers(id)
------------------------------------------------------------

-- Insert those customers

-- John, Doe
-- Jerome, Lalu
-- Lea, Rive
-----------------------------------------------------------
-- Insert those customer profiles, use subqueries
--
-- John is loggedIn
-- Jerome is not logged in

-- INSERT INTO customer_profile (isloggedin, customer_id)
-- SELECT true, id
-- FROM customer
-- WHERE first_name = 'John'
--
-- INSERT INTO customer_profile (isloggedin, customer_id)
-- SELECT false, id
-- FROM customer
-- WHERE first_name = 'Jerome'
------------------------------------------------------------


-- Insert those customer profiles, use subqueries

-- John is loggedIn
-- Jerome is not logged in
------------------------------------------------------------
-- INSERT INTO customer_profile (isLoggedIn, customer_id)
-- SELECT true, id
-- FROM customer
-- WHERE first_name = 'John'
------------------------------------------------------------
-- INSERT INTO customer_profile (isLoggedIn, customer_id)
-- SELECT false, id
-- FROM customer
-- WHERE first_name = 'Jerome'

------------------------------------------------------------

-- Use the relevant types of Joins to display:

-- The first_name of the LoggedIn customers

-- SELECT COUNT(*)
-- FROM customer c
-- LEFT JOIN customer_profile cp ON c.id = cp.customer_id
-- WHERE cp.isloggedin IS NULL OR cp.isloggedin = false;

-- All the customers first_name and isLoggedIn columns - even the customers those who don’t have a profile.

-- SELECT c.first_name, COALESCE(cp.isloggedin, false) AS isloggedin
-- FROM customer c
-- LEFT JOIN customer_profile cp ON c.id = cp.customer_id;

--     The number of customers that are not LoggedIn
-- SELECT COUNT(*)
-- FROM customer c
-- LEFT JOIN customer_profile cp ON c.id = cp.customer_id
-- WHERE cp.isloggedin IS NULL OR cp.isloggedin = false

------------------------------------------------------------





