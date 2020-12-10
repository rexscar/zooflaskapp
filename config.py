import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    SQL_SERVER = os.environ.get('SQL_SERVER') or '[reginald.database.windows.net]'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or '[regidata]'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or '[regiadmin]'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or '[R4e3g2i1]'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or '[reginaldstore]'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or '[5tcCLH8rfkAXAUgHRlAQAz2L1oKt1xD8Bc62RtNjLjYp9E7r6M9IOu4pu2HvwkSmp67YmO/g+pDiceT2QRDGcQ==]'
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or '[images]'
