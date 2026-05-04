
import os
import pytest

from planteye import create_app
from planteye.db import db as _db

db_uri = os.getenv('DATABASE_URL', 'sqlite3:///memory')
db_user = os.getenv('POSTGRES_USER', 'test')
db_pass = os.getenv('POSTGRES_PASSWORD', 'password123')

# TODO: setup fixtures

@pytest.fixture
def app():
    
    app = create_app({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': db_uri,
        'SQLALCHEMY_TRACK_MODIFICATIONS': False,
        })

    with app.app_context():
        from planteye import models

        _db.create_all()
        yield app
        _db.session.remove()
        _db.drop_all()

@pytest.fixture
def db(app):
    return _db

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()

@pytest.fixture
def user(app):
    from planteye.models.user import User
    user = User(email="test@example.com", password="hashed_pw")
    _db.session.add(user)
    _db.session.commit()















# TODO: create test DB
# TODO: write tests
