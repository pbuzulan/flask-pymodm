def _get_uri(db_username: str, db_password: str, db_host: str, db_port: str, db_name: str) -> str:
    username = db_username + ':' if db_username else ''
    password = db_password + '@' if db_password else ''
    conn_ = 'mongodb://' + username + password + db_host + ':' + db_port + '/' + db_name
    return conn_
