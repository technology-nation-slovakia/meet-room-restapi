.print Insert fake data

-- User John doe
INSERT INTO users (email, name, surname, password) VALUES  ("johndoe@home", "John", "Doe", "password");

-- rooms
INSERT INTO Places (name, description, id_remote, timeZone) VALUES ('Room 1', 'Green Room', 'cscoursetest1@gmail.com', 1);
INSERT INTO Places (name, description, id_remote, timeZone) VALUES ('Room 2', 'Blue Room', '19a82ol49q84c4sj4gdiimt9as@group.calendar.google.com', 1);
INSERT INTO Places (name, description, id_remote, timeZone) VALUES ('Room 3', 'Coffee Open Space', 'sglon18uoo029k7u91r5bsoeeg@group.calendar.google.com', 1);
INSERT INTO Places (name, description, id_remote, timeZone) VALUES ('Room 4', 'Terrace', 'oiv6geb1uda9lv1odgbhf5sjoo@group.calendar.google.com', 1);

-- events in room1
INSERT INTO items (name, description, start_date, end_date, user_id, place_id, itemtype_id) VALUES ('room1 Event #1','room1 desc Part1','2017-11-01 09:00:00', '2017-11-01 12:00:00', 1, 1, 1);
INSERT INTO items (name, description, start_date, end_date, user_id, place_id, itemtype_id) VALUES ('room1 Event #2','','2017-11-01 12:00:00', '2017-11-01 13:00:00', 1, 1, 1);
INSERT INTO items (name, description, start_date, end_date, user_id, place_id, itemtype_id) VALUES ('room1 Event #3','','2017-11-01 14:00:00', '2017-11-01 15:00:00', 1, 1, 1);
INSERT INTO items (name, description, start_date, end_date, user_id, place_id, itemtype_id) VALUES ('room1 Event #1','room1 desc Part2','2017-11-01 15:30:00', '2017-11-01 19:00:00', 1, 1, 1);

INSERT INTO items (name, description, start_date, end_date, user_id, place_id, itemtype_id) VALUES ('room1 Event #4','','2017-11-02 09:00:00', '2017-11-02 11:00:00', 1, 1, 1);
INSERT INTO items (name, description, start_date, end_date, user_id, place_id, itemtype_id) VALUES ('room1 Event #5','','2017-11-02 13:00:00', '2017-11-02 15:00:00', 1, 1, 1);
INSERT INTO items (name, description, start_date, end_date, user_id, place_id, itemtype_id) VALUES ('room1 Event #6','','2017-11-02 15:00:00', '2017-11-02 16:00:00', 1, 1, 1);

INSERT INTO items (name, description, start_date, end_date, user_id, place_id, itemtype_id) VALUES ('room1 Event #7','','2017-11-03 09:00:00', '2017-11-03 11:00:00', 1, 1, 1);
INSERT INTO items (name, description, start_date, end_date, user_id, place_id, itemtype_id) VALUES ('room1 Event #8','','2017-11-04 13:00:00', '2017-11-04 15:00:00', 1, 1, 1);
INSERT INTO items (name, description, start_date, end_date, user_id, place_id, itemtype_id) VALUES ('room1 Event #9','','2017-11-05 15:00:00', '2017-11-05 16:00:00', 1, 1, 1);

INSERT INTO items (name, description, start_date, end_date, user_id, place_id, itemtype_id) VALUES ('room1 Event #10','','2017-11-24 15:00:00', '2017-11-24 16:00:00', 1, 1, 1);
INSERT INTO items (name, description, start_date, end_date, user_id, place_id, itemtype_id) VALUES ('room1 Event #11','','2017-11-24 19:00:00', '2017-11-24 19:30:00', 1, 1, 1);
INSERT INTO items (name, description, start_date, end_date, user_id, place_id, itemtype_id) VALUES ('room1 Event #12','','2017-11-24 21:00:00', '2017-11-24 21:30:00', 1, 1, 1);

-- events room3
INSERT INTO items (name, description, start_date, end_date, user_id, place_id, itemtype_id) VALUES ('room3 Event #10','','2017-11-01 09:00:00', '2017-11-01 18:00:00', 1, 3, 1);
INSERT INTO items (name, description, start_date, end_date, user_id, place_id, itemtype_id) VALUES ('room3 Event #11','','2017-11-02 09:00:00', '2017-11-02 18:00:00', 1, 3, 1);
INSERT INTO items (name, description, start_date, end_date, user_id, place_id, itemtype_id) VALUES ('room3 Event #12','','2017-11-03 09:00:00', '2017-11-03 18:00:00', 1, 3, 1);

-- info room1
INSERT INTO items (name, description, start_date, end_date, user_id, place_id, itemtype_id) VALUES ('room1 Info #1','room1 Info #1 description','2017-11-01 09:00:00', '2017-11-01 18:00:00', 1, 1, 2);

-- alert room2
INSERT INTO items (name, description, start_date, end_date, user_id, place_id, itemtype_id) VALUES ('room2 Alert #1','room2 Alert #1 description','2017-11-01 09:00:00', '2017-11-01 18:00:00', 1, 2, 3);

-- message all room
INSERT INTO items (name, description, start_date, end_date, user_id, place_id, itemtype_id) VALUES ('All room message #1','this is message for all','2017-11-01 09:00:00', '2017-11-01 18:00:00', 1, NULL, 4);


select * from items;