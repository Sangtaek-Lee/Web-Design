CREATE TABLE users (
first_name TEXT NOT NULL,
last_name TEXT NOT NULL,
age INTEGER NOT NULL,
country TEXT NOT NULL,
phone TEXT NOT NULL,
balance INTEGER NOT NULL
);

SELECT * 
FROM users
WHERE age >= 30;

SELECT last_name, COUNT(*) FROM users
GROUP BY last_name
ORDER BY COUNT(*) DESC;