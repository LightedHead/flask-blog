from app import db
from datetime import datetime

class Article(db.Model):
    __tablename__ = 'article'
    title = db.Column(db.String(140),primary_key=True)
    body = db.Column(db.String(9999))
    timestamp = db.Column(db.DateTime,index=True,default=datetime.utcnow)
    user_id = db .Column(db.Integer,db.ForeignKey('user.id'))

    def __repr__(self):
        return '<article {}>'.format(self.title)