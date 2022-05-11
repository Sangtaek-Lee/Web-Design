-- SQLite
SELECT rowid, * FROM examples;


CREATE TABLE classmates (
id INTEGER PRIMARY KEY,
name TEXT
);

DROP TABLE classmates;

CREATE 
TABLE classmates (
name TEXT,
age INT,
address TEXT
);

INSERT
INTO classmates (name, age)
VALUES ('홍길동', 23);

INSERT
INTO classmates (name, age, address)
VALUES ('홍길동', 30, '서울');

INSERT
INTO classmates
VALUES ('홍길동', 30, '서울');

CREATE
TABLE classmates(
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
age INT NOT NULL,
address TEXT NOT NULL
);

INSERT
INTO classmates
VALUES (1, '홍길동', 30, '서울');

INSERT
INTO classmates(name, age, address)
VALUES ('홍길동', 30, '서울');




CREATE
TABLE classmates(
name TEXT NOT NULL,
age INT NOT NULL,
address TEXT NOT NULL
);

INSERT
INTO classmates
VALUES
('홍길동', 30, '서울'),
('김철수', 30, '대전'),
('이싸피', 26, '광주'),
('박삼성', 29, '구미'),
('최전자', 28, '부산');


SELECT rowid, name
FROM classmates
LIMIT 1 OFFSET 2;

SELECT rowid, name
FROM classmates
WHERE address='서울';

SELECT
DISTINCT age
FROM classmates;

DELETE
FROM classmates
WHERE rowid = 5;

INSERT
INTO classmates
VALUES ('최전자', 28, '부산');

UPDATE classmates
SET name='홍길동', address='제주도'
WHERE rowid=5;