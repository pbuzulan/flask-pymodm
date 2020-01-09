# Flask-PyMODM

[MongoDB](https://www.mongodb.com/) is a document-based database for general purpose use.

Flask-PyMODM is the bridge between Flask and PyMODM, it brings to developers a simplified way to use PyMODM in Flask applications.

# Quickstart

To start using Flask-PyMODM, install or update it via pip:
```
pip install Flask-PyMODM
```


### A Simple Example
 ```
from flask import Flask
from flask_pymodm import PyModm


def configure_app(app):
    app.config['MONGODB_DB_NAME'] = 'test'
    app.config['MONGODB_HOST'] = 'localhost'
    app.config['MONGODB_PORT'] = '27017'

def create_app():
    app = Flask(__name__)
    configure_app(app)
    PyModm(app)
    return app

if __name__ == '__main__':
    create_app().run(host='0.0.0.0', port=5000)
```


## Customizing Properties

In order to customize the host, add the following into your app.config (see [Configuration Handling](https://flask.palletsprojects.com/en/1.1.x/config/) for more details):
```
MONGODB_HOST = "10.10.10.13"                 # default is "localhost"
MONGODB_PORT = "27017"                       # default is "27017"
MONGODB_DB_NAME = "test"                     # default is "my-app"
MONGODB_ALIAS_CONNECTION = "my_connection"   # default is "default"
MONGODB_USERNAME = "my_username"             # default is None
MONGODB_PASSWORD = "my_password"             # default is None
```

## Test
To run test suite use the `tox` command.

Links
-----

-   Documentation: https://flask-sqlalchemy.palletsprojects.com/
-   Releases: 
-   Code: https://github.com/pbuzulan/flask-pymodm
-   Issue tracker: https://github.com/pbuzulan/flask-pymodm/issues
-   Test status: 
-   Test coverage: 
