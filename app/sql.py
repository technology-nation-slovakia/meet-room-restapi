# native SQL statements module
from app import app, db
import logging

def runSQL(statement):
    # execute SQL statement
    result = db.engine.execute(statement)

    # transforn result to array of rows
    rows = [dict(row) for row in result.fetchall()]

    # log statement
    if app.debug:
        app.logger.debug(statement)
        #print('rows count: ', len(rows))
        #print(rows)

    return rows

