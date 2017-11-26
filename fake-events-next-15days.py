#!/usr/bin/env python

from app.sql import runSQL

d = runSQL('''
     DELETE FROM items where date(start_date) >= date('now');
     ''')

for i in range(15):
    res = runSQL('''
        INSERT INTO items (name, description, start_date, end_date, user_id, place_id, itemtype_id)
        VALUES ('Event #1 ' || date('now', '+{0} days'), 'some description',
                datetime(date('now', '+{0} days'),'09:00'),
                datetime(date('now', '+{0} days'),'12:00'), 1, 1, 1);
        '''.format(i))

    res = runSQL('''
        INSERT INTO items (name, description, start_date, end_date, user_id, place_id, itemtype_id)
        VALUES ('Event #2 ' || date('now', '+{0} days'), 'some description',
                datetime(date('now', '+{0} days'),'13:00'),
                datetime(date('now', '+{0} days'),'16:00'), 1, 1, 1);
        '''.format(i))

    res = runSQL('''
        INSERT INTO items (name, description, start_date, end_date, user_id, place_id, itemtype_id)
        VALUES ('Event #3 ' || date('now', '+{0} days'), 'some description',
                datetime(date('now', '+{0} days'),'16:00'),
                datetime(date('now', '+{0} days'),'20:00'), 1, 1, 1);
        '''.format(i))

    res = runSQL('''
        INSERT INTO items (name, description, start_date, end_date, user_id, place_id, itemtype_id)
        VALUES ('Info @' || date('now', '+{0} days'), 'Info description',
                datetime(date('now', '+{0} days'),'10:00'),
                datetime(date('now', '+{0} days'),'18:00'), 1, 1, 2);
        '''.format(i))

    res = runSQL('''
        INSERT INTO items (name, description, start_date, end_date, user_id, place_id, itemtype_id)
        VALUES ('Alert @' || date('now', '+{0} days'), 'Alert description',
                datetime(date('now', '+{0} days'),'12:00'),
                datetime(date('now', '+{0} days'),'14:00'), 1, 1, 3);
        '''.format(i))

    res = runSQL('''
        INSERT INTO items (name, description, start_date, end_date, user_id, place_id, itemtype_id)
        VALUES ('Message @' || date('now', '+{0} days'), 'Message description',
                datetime(date('now', '+{0} days'),'08:00'),
                datetime(date('now', '+{0} days'),'20:00'), 1, 1, 4);
        '''.format(i))