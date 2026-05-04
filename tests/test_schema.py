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
def test_user_schema(app):
    tables = inspect(db.engine).get_table_names()
    column_dict = inspect(db.engine).get_columns('user')
    columns = [c['name'] for c in column_dict]

    assert 'user' in tables
    assert 'id' in columns
    assert 'email' in columns
    assert 'password' in columns

def test_plant_schema(app):
    tables = inspect(db.engine).get_table_names()
    column_dict = inspect(db.engine).get_columns('plant')
    columns = [c['name'] for c in column_dict]

    assert 'plant' in tables
    assert 'id' in columns
    assert 'type' in columns
    assert 'scientific_name' in columns
    assert 'name' in columns
    assert 'desc' in columns
    assert 'link' in columns
    assert 'slug' in columns
    assert 'updated' in columns
    assert 'created' in columns
    assert 'growth' in columns
    assert 'water' in columns
    assert 'light' in columns
    assert 'hardiness' in columns
    assert 'soil' in columns
    assert 'family' in columns

def test_plant_sensor_schema(app):
    tables = inspect(db.engine).get_table_names()
    column_dict = inspect(db.engine).get_columns('plant_sensor')
    columns = [c['name'] for c in column_dict]

    assert 'plant_sensor' in tables
    assert 'id' in columns
    assert 'plant_id' in columns
    assert 'type' in columns
    assert 'name' in columns
    assert 'light_reading' in columns
    assert 'water_reading' in columns
    assert 'soil' in columns

def test_ai_output_schema(app):
    tables = inspect(db.engine).get_table_names()
    column_dict = inspect(db.engine).get_columns('ai_output')
    columns = [c['name'] for c in column_dict]

    assert 'ai_output' in tables
    assert 'id' in columns
    assert 'plant_id' in columns
    assert 'created' in columns
    assert 'severity' in columns
    assert 'message' in columns





