import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '3b7d!@Ud4c1tyCMS#2025'

    # Storage account info
    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'image11project'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'M/tPRj5DIHWEYSEgDgaZP2uneZy9RyToRr8RIKv6DfysjMT9ZynUYonVKNu0rQb8BxWv49LtbcDt9LIFwKtsxQ=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'

    # SQL Server info
    SQL_SERVER = os.environ.get('SQL_SERVER') or 'cms1.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'cms'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'cmsadmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'CMS4dmin'
    # Connection string for SQLAlchemy
    SQLALCHEMY_DATABASE_URI = (
        'mssql+pyodbc://'
        + SQL_USER_NAME + '@' + SQL_SERVER + ':'
        + SQL_PASSWORD + '@' + SQL_SERVER
        + ':1433/' + SQL_DATABASE
        + '?driver=ODBC+Driver+17+for+SQL+Server'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET') or 'xw98Q~3YdeTQ3HqqyjgpnoPdLxYtfrbNW0YUDbXb'
    # In production, recommend using KeyVault or environment variables for CLIENT_SECRET

    AUTHORITY = os.environ.get('AUTHORITY') or "https://login.microsoftonline.com/common"  # For multi-tenant apps

    CLIENT_ID = os.environ.get('CLIENT_ID') or "e1b24baf-e14a-438b-acc1-d3cd88871c80"

    REDIRECT_PATH = "/getAToken"  # Must match your Azure app registration

    SCOPE = ["User.Read"]  # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache stored in server-side session
