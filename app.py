from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import date
import os
import sqlite3

# checks the instance folder for the blog.db file, if it doesn't exist, the file is created
db_path = os.path.join('instance', 'blog.db')
sql_path = 'blog.sql'

if not os.path.exists(db_path):
    with open(sql_path, 'r') as f:
        sql = f.read()
    conn = sqlite3.connect(db_path)
    conn.executescript(sql)
    conn.close()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)

# Association table for many-to-many relationship
post_tags = db.Table('post_tags',
    db.Column('post_id', db.Integer, db.ForeignKey('posts.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'), primary_key=True)
)

# Model for blog posts
class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    date = db.Column(db.String(20), nullable=False)
    excerpt = db.Column(db.Text, nullable=False)
    body = db.Column(db.Text, nullable=False)
    tags = db.relationship('Tag', secondary=post_tags, backref=db.backref('posts', lazy='dynamic'))

# Model for tags
class Tag(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)


#Page to show a single blog post
@app.route('/post/<int:post_id>')
def show_post(post_id):
    post = Post.query.get_or_404(post_id)
    post_tags = post.tags
    today = date.today().isoformat()
    return render_template('single_post_page.html', post=post, post_tags=post_tags, year=2025, current_date=today)

# Page to edit a blog post
@app.route('/edit/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    if request.method == 'POST':
        post.title = request.form['title']
        post.date = request.form['date']
        post.excerpt = request.form['excerpt']
        post.body = request.form['body']
        # Update tags
        tag_names = [t.strip() for t in request.form['tags'].split(',') if t.strip()]
        tags = []
        for name in tag_names:
            tag = Tag.query.filter_by(name=name).first()
            if not tag:
                tag = Tag(name=name)
                db.session.add(tag)
            tags.append(tag)
        post.tags = tags
        db.session.commit()
        return redirect(url_for('show_post', post_id=post.id))
    return render_template('edit_post.html', post=post, year=2025)

# Saving comments on a blog post
class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
    date = db.Column(db.String(20), nullable=False)
    title = db.Column(db.String(200), nullable=False)  
    content = db.Column(db.Text, nullable=False)
    post = db.relationship('Post', backref=db.backref('comments', lazy=True))

# Model to add and save comments made on a post
@app.route('/post/<int:post_id>/comment', methods=['POST'])
def add_comment(post_id):
    title = request.form['title']
    content = request.form['content']
    new_comment = Comment(
        post_id=post_id,
        date=date.today().isoformat(),
        title=title,
        content=content
    )
    db.session.add(new_comment)
    db.session.commit()
    return redirect(url_for('show_post', post_id=post_id))

# Creates the page to make a new blog post
@app.route('/create_post', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        tag_names = [t.strip().capitalize() for t in request.form['tags'].split(',') if t.strip()]
        tags = []
        for name in tag_names:
            tag = Tag.query.filter_by(name=name).first()
            if not tag:
                tag = Tag(name=name)
                db.session.add(tag)
            tags.append(tag)
        new_post = Post(
            title=request.form['title'],
            date=request.form['date'],
            excerpt=request.form['excerpt'],
            body=request.form['body'],
            tags=tags
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('show_post', post_id=new_post.id))
    return render_template('create_post.html', year=2025)

# creates the home page named 'simple-variables.html'
@app.route('/')
def home():
    posts = Post.query.order_by(Post.date.desc()).all()
    print(posts)
    return render_template('simple-variables.html', posts=posts, title='Home Page', who='everyone', year=2025)

# Create a page for tags
@app.route('/tags')
def tags():
    tags = Tag.query.all()
    for tag in tags:
        tag.post_count = tag.posts.count()
    return render_template('tags.html', tags=tags, title='Tags Overview', year=2025)

#search through tags
@app.route('/search_tags')
def search_tags():
    query = request.args.get('query', '')
    tags = Tag.query.filter(Tag.name.ilike(f'%{query}%')).all()
    for tag in tags:
        tag.post_count = tag.posts.count()
    return render_template('tags.html', tags=tags, title='Tags', query=query, year=2025)

# route to show posts linked to spesific tag
@app.route('/tag/<int:tag_id>')
def show_tag(tag_id):
    tag = Tag.query.get_or_404(tag_id)
    posts = tag.posts  # This uses the relationship
    return render_template('blogarchive.html', posts=posts, title=f'Posts tagged "{tag.name}"', year=2025)

# create blog archive
@app.route('/blogarchive')
def blogarchive():
    posts = Post.query.order_by(Post.date.desc()).all()
    return render_template('blogarchive.html', posts=posts, title='Blog Archive', year=2025)

if __name__ == '__main__':
    app.run(debug=True)