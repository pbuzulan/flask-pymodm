import pymodm
from flask_pymodm.util import _get_uri

__all__ = ['connect']


def connect(config=None, **kwargs):
    """
    Given Flask application's config dict, extract relevant config vars
    out of it and establish Pymodm connection based on them.
    """
    # Validate that the config is a dict
    if config is None or not isinstance(config, dict):
        raise TypeError('Application configuration cannot be None or {}'.format(type(config)))

    db_username = config.get('MONGODB_USERNAME')
    db_password = config.get('MONGODB_PASSWORD')
    db_host = config.get('MONGODB_HOST')
    db_port = config.get('MONGODB_PORT')
    db_name = config.get('MONGODB_DB_NAME')
    db_connection_alias = config.get('MONGODB_ALIAS_CONNECTION')
    mongodb_options = kwargs
    pymodm.connect(
        _get_uri(db_username=db_username, db_password=db_password, db_host=db_host, db_port=db_port,
                 db_name=db_name), alias=db_connection_alias, **mongodb_options)
    return pymodm.connection._get_connection(alias=db_connection_alias)
