"""Blogly application."""

from flask import Flask, request, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Post, Tag, PostTag


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "NGE4ev"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/')
def show_homepage():
    return redirect('/users')

@app.route('/users')
def show_users():
    users = User.query.all()
    return render_template('users.html', users=users)

@app.route('/users/<int:user_id>')
def show_user_detail(user_id):
    user = User.query.get_or_404(user_id)
    return render_template("users/details.html", user=user)

@app.route('/users/new')
def show_create_user_form():
    return render_template ('users/new.html')

@app.route('/users/new', methods=["POST"])
def create_new_user():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    img_url = request.form["img_url"]
    
    new_user = User(first_name=first_name, last_name=last_name, img_url=img_url)
    db.session.add(new_user)
    db.session.commit()
    
    return redirect("/users")

@app.route('/users/<int:user_id>/edit')
def show_edit_form(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('users/edit.html', user=user)

@app.route('/users/<int:user_id>/edit', methods=["POST"])
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    user.first_name = request.form["first_name"]
    user.last_name = request.form["last_name"]
    user.img_url = request.form["img_url"]
    
    db.session.add(user)
    db.session.commit()
    
    return redirect("/users")

@app.route('/users/<int:user_id>/delete', methods=["POST"])
def delete_user(user_id):

    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect("/users")

@app.route('/users/<int:user_id>/posts/new')
def new_post_form(user_id):
    user = User.query.get_or_404(user_id)
    tags = Tag.query.all()
    return render_template('posts/submit-post.html', user=user, tags=tags)

# @app.route('/users/<int:user_id>/posts/new', methods=["POST"])
# def new_post(user_id):
#     user = User.query.get_or_404(user_id)
#     new_post = Post(title=request.form['title'],
#                     content=request.form['content'],
#                     user=user)
    
#     db.session.add(new_post)
#     db.session.commit
    
#     return redirect(f"/users/{user_id}")

@app.route('/users/<int:user_id>/posts/new', methods=["POST"])
def posts_new(user_id):

    user = User.query.get_or_404(user_id)
    tag_ids = [int(num) for num in request.form.getlist("tags")]
    tags = Tag.query.filter(Tag.id.in_(tag_ids)).all()
    new_post = Post(title=request.form['title'],
                    content=request.form['content'],
                    user=user, tags=tags)

    db.session.add(new_post)
    db.session.commit()

    return redirect(f"/users/{user_id}")

@app.route('/posts/<int:post_id>')
def show_post(post_id):
    post = Post.query.get_or_404(post_id)
    tags = Tag.query.all()
    
    return render_template("posts/show.html", post=post, tags=tags)

@app.route('/posts/<int:post_id>/edit')
def show_post_edit_form(post_id):
    post = Post.query.get_or_404(post_id)
    tags = Tag.query.all()
    return render_template('posts/edit.html', post=post, tags=tags)

@app.route('/posts/<int:post_id>/edit', methods=["POST"])
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    post.title = request.form["title"]
    post.content = request.form["content"]
    tag_ids = [int(num) for num in request.form.getlist("tags")]
    post.tags = Tag.query.filter(Tag.id.in_(tag_ids)).all()
    
    db.session.add(post)
    db.session.commit()
    
    return redirect(f"/posts/{post_id}")

@app.route('/posts/<int:post_id>/delete', methods=["POST"])
def delete_post(post_id):

    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()

    return redirect("/users")

@app.route('/tags')
def show_tags():
    tags = Tag.query.all()
    return render_template('tags/tags.html', tags=tags)

@app.route('/tags/<int:tag_id>')
def show_tag_details(tag_id):
    tag = Tag.query.get_or_404(tag_id)
    return render_template('tags/details.html', tag=tag)

@app.route('/tags/<int:tag_id>/edit')
def show_tag_edit_form(tag_id):
    tag = Tag.query.get_or_404(tag_id)
    return render_template('tags/edit.html', tag=tag)

@app.route('/tags/<int:tag_id>/edit', methods=["POST"])
def edit_tag(tag_id):
    tag = Tag.query.get_or_404(tag_id)
    tag.name = request.form['tag-name']
    
    db.session.add(tag)
    db.session.commit()
    
    return redirect('/tags')

@app.route('/tags/new')
def show_add_tag_form():    
    return render_template('/tags/new.html')

@app.route('/tags/new', methods=["POST"])
def add_tag():
    tag = Tag(name=request.form['tag-name'])
    db.session.add(tag)
    db.session.commit()
    
    return redirect('/tags')

@app.route('/tags/<int:tag_id>/delete', methods=["POST"])
def delete_tag(tag_id):
    tag = Tag.query.get_or_404(tag_id)
    db.session.delete(tag)
    db.session.commit()
    
    return redirect('/tags')