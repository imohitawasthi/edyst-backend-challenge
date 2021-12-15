from src import db

import datetime


class CrawledPage(db.Model):
    __tablename__ = 'crawled_pages'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    url = db.Column(db.String)
    word_count = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    modified_at = db.Column(db.DateTime, default=datetime.datetime.now())
