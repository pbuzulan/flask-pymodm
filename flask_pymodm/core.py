# -*- coding: utf-8 -*-
from flask import Flask, current_app

from flask_pymodm.connection import connect


class PyModm(object):
    mongodb_options = None

    def __init__(self, app=None, **kwargs):
        self.app = None
        if app is None or not isinstance(app, Flask):
            raise Exception('Invalid Flask application instance')

        self.init_app(app, **kwargs)

    def init_app(self, app, **kwargs):
        app.config.setdefault('MONGODB_HOST', 'localhost')
        app.config.setdefault('MONGODB_PORT', '27017')
        app.config.setdefault('MONGODB_DB_NAME', 'my-app')
        app.config.setdefault('MONGODB_USERNAME', None)
        app.config.setdefault('MONGODB_PASSWORD', None)
        app.config.setdefault('MONGODB_ALIAS_CONNECTION', 'default')

        self.mongodb_options = kwargs
        app.teardown_appcontext(self.teardown)
        self.app = app
        if 'mongodb' not in app.extensions:
            app.extensions['mongodb'] = {}

        if self in app.extensions['mongodb']:
            # Raise an exception if extension already initialized as
            # potentially new configuration would not be loaded.
            raise Exception('Extension already initialized')

        s = {'app': app, 'conn': connect(config=app.config)}
        app.extensions['mongodb'][self] = s

    @property
    def connection(self):
        """
        Return MongoDB connection associated with this PyModm instance.
        """
        return current_app.extensions['mongodb'][self]['conn']

    def teardown(self, exception):
        current_app.extensions['mongodb'][self] = None
        return current_app.extensions['mongodb'][self]
