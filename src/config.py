import os

SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))
# Enable debug mode.
DEBUG = True
# Connect to the database
SQLALCHEMY_DATABASE_URI = 'sqlite:///crawler.db'
# Turn off the Flask-SQLAlchemy event system and warning
SQLALCHEMY_TRACK_MODIFICATIONS = False

REDIS_HOST = '0.0.0.0'
REDIS_PORT = 6379

APPLICATION_URL = '0.0.0.0'
APPLICATION_PORT = 9000
