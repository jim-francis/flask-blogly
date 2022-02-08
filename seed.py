from models import User, Post, db
from app import app

db.drop_all()
db.create_all()

u1 = User(first_name="Jimmy", last_name="Francis", 
          img_url="/static/imgs/ostrich.jpeg")

u2 = User(first_name="Beth", last_name="Francis",
          img_url="/static/imgs/bird.jpeg")

db.session.add_all([u1, u2])
db.session.commit()

p1 = Post(title="Hello World", 
          content="Hi, how are you fine thank you.",
          user_id="1")

db.session.add(p1)
db.session.commit()