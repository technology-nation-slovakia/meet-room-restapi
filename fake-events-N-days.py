#!/usr/bin/env python

import argparse
from app.sql import runSQL

parser = argparse.ArgumentParser(description='Fake items insert')
parser.add_argument('days', metavar='N', type=int, help='Number of days')
args = parser.parse_args()

print('Fake data insert for {} days'.format(args.days))

# runSQL('''
#      DELETE FROM items where date(start_date) >= date('now');
#      ''')

for i in range(args.days):
    for j in range (4):
        runSQL('''
            INSERT INTO items (name, description, start_date, end_date, user_id, place_id, itemtype_id)
            VALUES ('0-1am 1h event ' || date('now', '+{0} days'), 'some description',
                    datetime(date('now', '-1 days','+{0} days'),'00:00 +01:00'),
                    datetime(date('now', '+{0} days'),'01:00 +01:00'), 1, {1}, 1);
            '''.format(i, j+1))

        runSQL('''
            INSERT INTO items (name, description, start_date, end_date, user_id, place_id, itemtype_id)
            VALUES ('1-2am 1h event ' || date('now', '+{0} days'), 'some description',
                    datetime(date('now', '+{0} days'),'01:00+01:00'),
                    datetime(date('now', '+{0} days'),'02:00+01:00'), 1, {1}, 1);
            '''.format(i, j+1))

        runSQL('''
            INSERT INTO items (name, description, start_date, end_date, user_id, place_id, itemtype_id)
            VALUES ('8-9am 1h event ' || date('now', '+{0} days'), 'some description',
                    datetime(date('now', '+{0} days'),'08:00+01:00'),
                    datetime(date('now', '+{0} days'),'09:00+01:00'), 1, {1}, 1);
            '''.format(i, j+1))

        runSQL('''
            INSERT INTO items (name, description, start_date, end_date, user_id, place_id, itemtype_id)
            VALUES ('9am-14pm 5H meeting ' || date('now', '+{0} days'), 'some description',
                    datetime(date('now', '+{0} days'),'09:00+01:00'),
                    datetime(date('now', '+{0} days'),'14:00+01:00'), 1, {1}, 1);
            '''.format(i, j+1))

        runSQL('''
            INSERT INTO items (name, description, start_date, end_date, user_id, place_id, itemtype_id)
            VALUES ('15-19pm 4H Event ' || date('now', '+{0} days'), 'some description',
                    datetime(date('now', '+{0} days'),'15:00+01:00'),
                    datetime(date('now', '+{0} days'),'19:00+01:00'), 1, {1}, 1);
            '''.format(i, j+1))

    # runSQL('''
    #     INSERT INTO items (name, description, start_date, end_date, user_id, place_id, itemtype_id, id_remote)
    #     VALUES ('Info @' || date('now', '+{0} days'), 'Info description',
    #             datetime(date('now', '+{0} days'),'10:00'),
    #             datetime(date('now', '+{0} days'),'18:00'), 1, 1, 2);
    #     '''.format(i, j+1))

    # runSQL('''
    #     INSERT INTO items (name, description, start_date, end_date, user_id, place_id, itemtype_id, id_remote)
    #     VALUES ('Alert @' || date('now', '+{0} days'), 'Alert description',
    #             datetime(date('now', '+{0} days'),'12:00'),
    #             datetime(date('now', '+{0} days'),'14:00'), 1, 1, 3);
    #     '''.format(i, j+1))

    # runSQL('''
    #     INSERT INTO items (name, description, start_date, end_date, user_id, place_id, itemtype_id, id_remote)
    #     VALUES ('Message @' || date('now', '+{0} days'), 'Message description',
    #             datetime(date('now', '+{0} days'),'08:00'),
    #             datetime(date('now', '+{0} days'),'20:00'), 1, 1, 4);
    #     '''.format(i, j+1))