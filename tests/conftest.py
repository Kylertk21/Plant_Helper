
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
def user_data(app):
    from planteye.models.user import User
    user = User(email="test@example.com", password="hashed_pw")
    _db.session.add(user)
    _db.session.commit()

@pytest.fixture
def plant_data(app):
    from planteye.models.plant import Plant
    plant = Plant(
            type="Plant",
            scientific_name="Morus alba",
            name="White mulberry",
            desc="Young leaves are edible.",
            link="/plants/morus-alba-white-mulberry",
            slug="morus-alba-white-mulberry",
            updated="2022-07-30T08:17:26.658Z",
            created="2020-08-11T16:09:47.485Z",
            growth="Medium",
            water="Moist",
            light="Full sun, partial sun/shade",
            hardiness="3-9",
            soil="Light (sandy), medium, heavy (clay)",
            family="Moraceae"
            )


    #TODO: finish plant fixture












# TODO: create test DB
# TODO: write tests
