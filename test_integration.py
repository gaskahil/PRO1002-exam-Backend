import os
import tempfile
import pytest
from app import app, db, Post, Tag, Comment

@pytest.fixture
def test_client():
    db_fd, db_path = tempfile.mkstemp()
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
    app.config['TESTING'] = True
    client = app.test_client()

    with app.app_context():
        db.create_all()

    yield client

    os.close(db_fd)
    os.unlink(db_path)

def test_create_and_query_post(test_client):
    with app.app_context():
        post = Post(title='Integration Test', date='2025-06-03', excerpt='ex', body='body')
        db.session.add(post)
        db.session.commit()
        queried = Post.query.filter_by(title='Integration Test').first()
        assert queried is not None
        assert queried.body == 'body'

def test_tag_relationship(test_client):
    with app.app_context():
        tag = Tag(name='TestTag')
        post = Post(title='Tagged Post', date='2025-06-03', excerpt='ex', body='body', tags=[tag])
        db.session.add(post)
        db.session.commit()
        queried_tag = Tag.query.filter_by(name='TestTag').first()
        assert queried_tag.posts.count() == 1
        assert queried_tag.posts.first().title == 'Tagged Post'

def test_comment_relationship(test_client):
    with app.app_context():
        post = Post(title='Commented Post', date='2025-06-03', excerpt='ex', body='body')
        db.session.add(post)
        db.session.commit()
        comment = Comment(post_id=post.id, date='2025-06-03', title='Test Comment', content='Nice!')
        db.session.add(comment)
        db.session.commit()
        queried_post = Post.query.get(post.id)
        assert len(queried_post.comments) == 1
        assert queried_post.comments[0].content == 'Nice!'