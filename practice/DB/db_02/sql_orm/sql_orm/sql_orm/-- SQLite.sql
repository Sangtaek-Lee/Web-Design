-- SQLite
SELECT count(*) FROM users_user;

SELECT * FROM users_user;

INSERT INTO users_user (first_name, last_name, age, country, phone, balance)
VALUES ('이름', '성', '20', '지역', '010-0000-0000', '5000000');

INSERT INTO users_user (first_name, last_name, age, country, balance) 
VALUES ('이름', '성', '20', '지역', '5000000');

SELECT *
FROM users_user
WHERE id = 102;

UPDATE users_user
SET first_name = '철수'
WHERE id = 102;

DELETE
FROM users_user
WHERE id = 101;

SELECT count(*)
FROM users_user;

SELECT first_name
FROM users_user
WHERE age=30;

SELECT count(*)
FROM users_user
WHERE age >= 30;

SELECT count(*)
FROM users_user
WHERE age <= 20;

SELECT count(*)
FROM users_user
WHERE age = 30 and last_name = '김';

SELECT count(*)
FROM users_user
WHERE age = 30 or last_name = '김';

SELECT count(*)
FROM users_user
WHERE phone LIKE '02%';

SELECT first_name
FROM users_user
WHERE country = '강원도' and last_name = '황';

SELECT *
FROM users_user
ORDER BY age DESC
LIMIT 10;

SELECT *
FROM users_user
ORDER BY balance ASC
LIMIT 10;

SELECT *
FROM users_user
ORDER BY balance ASC, age DESC
LIMIT 10;

SELECT *
FROM users_user
ORDER BY last_name DESC, first_name ASC
LIMIT 1
OFFSET 4;

SELECT avg(age)
FROM users_user
WHERE last_name = '김';

SELECT avg(balance)
FROM users_user
WHERE country = '강원도';

SELECT sum(balance)
FROM users_user;

SELECT country, count(*)
FROM users_user
GROUP BY country;