# -*- coding: utf-8 -*-
import pymodm

# Find the stack on which we want to store the database connection.
# Starting with Flask 0.9, the _app_ctx_stack is the correct one,
# before that we need to use the _request_ctx_stack.
try:
    from flask import _app_ctx_stack as stack
except ImportError:
    from flask import _request_ctx_stack as stack


class PyModm(object):
    def __init__(self, app=None, **kwargs):
        self.app = app
        if app is not None:
            self.init_app(app, **kwargs)

    def init_app(self, app, **kwargs):
        app.config.setdefault('MONGODB_HOST', 'localhost')
        app.config.setdefault('MONGODB_PORT', '27017')
        app.config.setdefault('MONGODB_DB_NAME', 'my-app')
        app.config.setdefault('MONGODB_USERNAME', None)
        app.config.setdefault('MONGODB_PASSWORD', None)
        app.config.setdefault('MONGODB_ALIAS_CONNECTION', 'default')

        # Use the newstyle teardown_appcontext if it's available,
        # otherwise fall back to the request context
        if hasattr(app, 'teardown_appcontext'):
            app.teardown_appcontext(self.teardown)
        else:
            app.teardown_request(self.teardown)

    def __getattr__(self, item, **kwargs):
        ctx = stack.top
        if ctx is not None:
            if not hasattr(ctx, 'mongodb'):
                username = ctx.app.config.get('MONGODB_USERNAME') + ':' if isinstance(
                    ctx.app.config.get('MONGODB_USERNAME'), str) else ''
                password = ctx.app.config.get('MONGODB_PASSWORD') + '@' if isinstance(
                    ctx.app.config.get('MONGODB_PASSWORD'), str) else ''

                ctx.mongodb = pymodm.connect(
                    'mongodb://' + username + password + ctx.app.config.get('MONGODB_HOST') + ctx.app.config.get(
                        'MONGODB_PORT') + ctx.app.config.get('MONGODB_DB_NAME'),
                    alias=ctx.app.config.get('MONGODB_ALIAS_CONNECTION'), **kwargs)

            return getattr(ctx.mongodb, item)

    def teardown(self, exception):
        ctx = stack.top
        if hasattr(ctx, 'mongodb'):
            ctx.mongodb = None
