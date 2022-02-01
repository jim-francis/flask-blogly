from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

"""Models for Blogly."""

class User(db.model):
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