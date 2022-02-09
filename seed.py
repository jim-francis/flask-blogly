from models import User, Post, Tag, PostTag, db
from app import app

db.drop_all()
db.create_all()

u1 = User(first_name="Jimmy", last_name="Francis", 
          img_url="/static/imgs/ostrich.jpeg")
u2 = User(first_name="Beth", last_name="Francis",
          img_url="/static/imgs/bird.jpeg")
u3 = User(first_name="Bugs", last_name="Rabbit",
          img_url="/static/imgs/rabbit.jpeg")

db.session.add_all([u1, u2, u3])
db.session.commit()

p1 = Post(title="Hello World", 
          content="Hi, how are you fine thank you.",
          user_id="1")
p2 = Post(title="Hi again", 
          content="Are you still there? Please advice.",
          user_id="1")
p3 = Post(title="Hi there", 
          content="Hey hey",
          user_id="2")
p4 = Post(title="Eat your vegetable", 
          content="Buddy please won't ya",
          user_id="3")

db.session.add_all([p1, p2, p3, p4])
db.session.commit()

t1 = Tag(name="insightful")
t2 = Tag(name="disgusting")
t3 = Tag(name="salacious")
t4 = Tag(name="exhausting")

db.session.add_all([t1,t2,t3,t4])
db.session.commit()