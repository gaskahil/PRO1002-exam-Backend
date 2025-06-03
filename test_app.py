import os
import tempfile
import pytest
from app import app, db, Post, Tag, Comment

@pytest.fixture
def client():
    db_fd, db_path = tempfile.mkstemp()
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
    app.config['TESTING'] = True
    client = app.test_client()

    with app.app_context():
        db.create_all()

    yield client

    os.close(db_fd)
    os.unlink(db_path)

def test_create_post(client):
    response = client.post('/create_post', data={
        'title': 'Test Post',
        'date': '2025-06-03',
        'excerpt': 'Test excerpt',
        'body': 'Test body',
        'tags': 'TestTag'
    }, follow_redirects=True)
    assert b'Test Post' in response.data

def test_view_post(client):
    with app.app_context():
        post = Post(title='View Post', date='2025-06-03', excerpt='ex', body='body')
        db.session.add(post)
        db.session.commit()
        post_id = post.id
    response = client.get(f'/post/{post_id}')
    assert b'View Post' in response.data

def test_edit_post(client):
    with app.app_context():
        post = Post(title='Edit Post', date='2025-06-03', excerpt='ex', body='body')
        db.session.add(post)
        db.session.commit()
        post_id = post.id
    response = client.post(f'/edit/{post_id}', data={
        'title': 'Edited Post',
        'date': '2025-06-03',
        'excerpt': 'ex',
        'body': 'new body',
        'tags': ''
    }, follow_redirects=True)
    assert b'Edited Post' in response.data

def test_add_comment(client):
    with app.app_context():
        post = Post(title='Comment Post', date='2025-06-03', excerpt='ex', body='body')
        db.session.add(post)
        db.session.commit()
        post_id = post.id
    response = client.post(f'/post/{post_id}/comment', data={
        'title': 'Comment Title',
        'content': 'Nice post!'
    }, follow_redirects=True)
    assert b'Comment Title' in response.data
    assert b'Nice post!' in response.data