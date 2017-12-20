#!/usr/bin/env python

# Meet Room Watch RESTful API server module
from app import app
from app.console_log import console_log

console_log(app.config['API_NAME'] + ' version {}'.format(app.config['API_VERSION']), 'note')

app.run(host=app.config['HOST'], port=app.config['PORT'])
