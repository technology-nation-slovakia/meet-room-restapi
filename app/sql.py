# native SQL statements module
from app import app, db
import logging
import re

def runSQL(statement):
    # execute SQL statement
    result = db.engine.execute(statement)

    # log statement
    if app.debug:
        app.logger.debug(statement)

    if re.search(r"^\s*SELECT", statement, re.I):
        # transforn result to array of rows
        rows = [dict(row) for row in result.fetchall()]
        if app.debug:
            print('Rows: ', len(rows))

        if len(rows) == 1:      # in case of result contains single item => return object
            rows = rows[0]
        elif len(rows) == 0:    # empty result
            rows = {}

        return rows

    elif re.search(r"^\s*INSERT", statement, re.I):
        if app.debug:
            print('Inserted ID: ', result.lastrowid)
        return result.lastrowid

    elif re.search(r"^\s*(?:DELETE|UPDATE)", statement, re.I):
        if app.debug:
            print('Deleted/Updated: ', result.rowcount)
        return result.rowcount



