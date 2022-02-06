import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

"""Models for Blogly."""

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    
    first_name = db.Column(db.String(20),
                           nullable=False)
    
    last_name = db.Column(db.String(20),
                          nullable=True)
    
    img_url = db.Column(db.String,
                        nullable=True)
    
    def __repr__(self):
        u = self
        return f"<User ID={u.id} first_name={u.first_name} last_name={u.last_name} img_url={u.img_url}>"
    
class Post(db.Model):
    __tablename__ = 'posts'
    
    id = db.Column(db.Integer,
                   primary_key=True, autoincrement=True)
    
    title = db.Column(db.Text, nullable=False)
    
    content = db.Column(db.Text, nullable=False)
    
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)