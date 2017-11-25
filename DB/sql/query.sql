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