-- test statements

SELECT items.id as id, items.name as name, items.description as description, start_date, end_date, isPrivate, users.id as user_id,
    users.name || ' ' || users.surname as user, places.id as place_id, places.name as place, item_type.id as type_id,
    item_type.name as type
FROM items, users, places, item_type
WHERE items.user_id = users.id
AND items.place_id = places.id
AND items.itemtype_id = item_type.id;

-- test
SELECT *
FROM items
WHERE place_ID = 1
    AND itemtype_ID = 1
    AND start_date <= datetime('now')
    AND datetime('now') <= end_date;

-- select items like in GC
SELECT * FROM items
WHERE (start_date < datetime('2017-12-10T00:30:00Z') AND datetime('2017-12-10T00:30:00Z') < end_date)
OR (datetime('2017-12-10T00:30:00Z') <= start_date AND end_date <= datetime('2017-12-10T10:00:00Z'))
OR (start_date < datetime('2017-12-10T10:00:00Z') AND datetime('2017-12-10T10:00:00Z') < end_date)
;

UPDATE items
SET updated = 0
WHERE not ifnull(id_remote,1)
AND place_id = 1
AND ((start_date < '2017-12-09T23:00:00Z' AND '2017-12-09T23:00:00Z' < end_date)
    OR ('2017-12-09T23:00:00Z' <= start_date AND end_date <= '2017-12-10T22:59:00Z')
    OR (start_date < '2017-12-10T22:59:00Z' AND '2017-12-10T22:59:00Z' < end_date));