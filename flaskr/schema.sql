DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS shop;
DROP TABLE IF EXISTS pricelist;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE shop (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    shopname TEXT UNIQUE NOT NULL,
    icon TEXT,
    location TEXT,
    description TEXT
);

CREATE TABLE pricelist (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
	shop_id INTEGER NOT NULL,
	category TEXT,
	title TEXT NOT NULL,
	price INTEGER NOT NULL,
	FOREIGN KEY (shop_id) REFERENCES shop (id)
);

INSERT INTO user (username, password)
VALUES ('admin', 'admin');

-- INSERT INTO shop (shopname, location)
-- VALUES 
-- ('shopname1', 'place1'),
-- ('shopname2', 'place2'),
-- ('shopname3', 'place3'),
-- ('shopname4', 'place4'),
-- ('shopname5', 'place5');

INSERT INTO pricelist (shop_id, title, price)
VALUES
(0, 'hair1', 1000),
(1, 'hair1', 1000),
(2, 'hair1', 1000),
(3, 'hair1', 1000),
(4, 'hair1', 1000),
(0, 'hair2', 110);