# native SQL statements module
from app import app, db
import logging

def runSQL(statement):
    # execute SQL statement
    result = db.engine.execute(statement)

    # transforn result to array of rows
    rows = [dict(row) for row in result.fetchall()]

    if len(rows) == 1:
        rows = rows[0]
    elif len(rows) == 0:
        rows = {}


    # log statement
    if app.debug:
        app.logger.debug(statement)
        #print('rows count: ', len(rows))
        #print(rows)

    return rows

