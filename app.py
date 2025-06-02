from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import date

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    date = db.Column(db.String(20), nullable=False)
    excerpt = db.Column(db.Text, nullable=False)
    body = db.Column(db.Text, nullable=False)
    tags = db.Column(db.String(200), nullable=True)  # Store as comma-separated string

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/post/<int:post_id>')
def show_post(post_id):
    post = Post.query.get_or_404(post_id)
    post_tags = [tag.strip() for tag in post.tags.split(',')] if post.tags else []
    today = date.today().isoformat()
    return render_template('single_post_page.html', post=post, post_tags=post_tags, year=2025, current_date=today)


@app.route('/create_post', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        tags = request.form['tags']
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

@app.route('/')
def home():
    posts = Post.query.order_by(Post.date.desc()).all()
    return render_template('simple-variables.html', posts=posts, title='Home Page', who='everyone', year=2025)

@app.route('/blogarchive')
def blogarchive():
    posts = Post.query.order_by(Post.date.desc()).all()
    return render_template('blogarchive.html', posts=posts, year=2025)

if __name__ == '__main__':
    app.run(debug=True)