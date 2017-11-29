.print DROP Tables

--Drop tables
DROP TABLE IF EXISTS items;
DROP TABLE IF EXISTS item_type;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS places;

----
.print CREATE Tables

--Create USERS Table
CREATE TABLE Users (
id          INTEGER     PRIMARY KEY AUTOINCREMENT,
email       TEXT        NOT NULL UNIQUE,
name        TEXT        NOT NULL,
surname     TEXT        NOT NULL,
reg_date    DATETIME    NOT NULL DEFAULT CURRENT_TIMESTAMP,
password    TEXT        NOT NULL,
admin       BOOLEAN     DEFAULT 0
);

-- Create table Places
CREATE TABLE Places (
id          INTEGER     PRIMARY KEY AUTOINCREMENT,
name        TEXT        NOT NULL UNIQUE,
description TEXT,
id_remote   TEXT
);

INSERT INTO Places (name, id_remote) VALUES ('Room 1', 'cscoursetest1@gmail.com');
INSERT INTO Places (name, id_remote) VALUES ('Room 2', '19a82ol49q84c4sj4gdiimt9as@group.calendar.google.com');
INSERT INTO Places (name, id_remote) VALUES ('Room 3', 'sglon18uoo029k7u91r5bsoeeg@group.calendar.google.com');
INSERT INTO Places (name, id_remote) VALUES ('Room 4', 'oiv6geb1uda9lv1odgbhf5sjoo@group.calendar.google.com');

-- Create table item_type
CREATE TABLE Item_type (
id          INTEGER     PRIMARY KEY,
name        TEXT        NOT NULL
);

INSERT INTO Item_type (id, name) VALUES (1, 'event');
INSERT INTO Item_type (id, name) VALUES (2, 'info');
INSERT INTO Item_type (id, name) VALUES (3, 'alert');
INSERT INTO Item_type (id, name) VALUES (4, 'message');


-- Create table Items
CREATE TABLE Items (
id          INTEGER     PRIMARY KEY AUTOINCREMENT,
name        TEXT        NOT NULL,
description TEXT,
start_date  DATETIME    NOT NULL,
end_date    DATETIME    NOT NULL,
isPrivate   BOOLEAN     DEFAULT 0,
user_id     INTEGER     NOT NULL REFERENCES users (id),
place_id    INTEGER     REFERENCES          places (id),
itemtype_id INTEGER     REFERENCES          item_type (id),
id_remote   TEXT,
updated     BOOLEAN     DEFAULT 0
);

-----------
.tables