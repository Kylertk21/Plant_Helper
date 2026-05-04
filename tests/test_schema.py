import pytest
from sqlalchemy import inspect, text
from planteye.db import db

def test_connection(app):
    with app.app_context():
        result = db.session.execute(text('SELECT 1'))
        assert result.scalar() == 1

def test_is_postgres(app):
    assert 'postgresql' in app.config['SQLALCHEMY_DATABASE_URI']

# Inspect for user in db table
def test_user_in_schema(app):
    tables = inspect(db.engine).get_table_names()
    assert 'user' in tables
