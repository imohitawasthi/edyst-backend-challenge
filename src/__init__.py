__version__ = '0.1'

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.config import REDIS_PORT, REDIS_HOST

from redis import Redis
from rq import Queue

redis_connection = Redis(
    host=REDIS_HOST,
    port=REDIS_PORT
)
redis_queue = Queue(connection=redis_connection)

app = Flask(__name__)
app.config.from_object('src.config')

db = SQLAlchemy(app)

from src.controllers import *


@app.before_first_request
def create_tables():
    db.create_all()
