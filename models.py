from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64))
    title = db.Column(db.String(255))
    content = db.Column(db.Text)
    password = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now(), default=datetime.now())

    @property
    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'title': self.title,
            'content': self.content,
            'password': self.password,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    postid = db.Column(db.Integer, db.ForeignKey('posts.id', ondelete='CASCADE'))
    post = db.relationship('Post', backref = 'comment_set')
    username = db.Column(db.String(64), nullable=False)
    content = db.Column(db.Text)
    parent_id = db.Column(db.Integer, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.now())

    @property
    def serialize(self):
        return {
            'id': self.id,
            'postid': self.postid,
            'username': self.username,
            'content': self.content,
            'parent_id': self.parent_id,
            'created_at': self.created_at
        }