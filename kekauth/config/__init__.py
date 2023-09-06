class FlaskConfig(object):
    DEBUG = True
    JSON_AS_ASCII = True
    JSON_SORT_KEYS = True
    SECRET_KEY = 'agsakhvsouwenelsp'
    DB_NAME = "metadata2.db"
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DB_NAME}'