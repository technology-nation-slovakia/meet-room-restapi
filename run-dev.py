#!/usr/bin/env python

# Meet Room Watch RESTful API server module
# Dev. version

from app import app

print(app.config['API_NAME'],'version {}'.format(app.config['API_VERSION']))

app.run(host = app.config['HOST'],
        port = app.config['PORT'])
