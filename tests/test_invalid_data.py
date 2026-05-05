import pytest
from sqlalchemy.exc import IntegrityError
from planteye.db import db as _db


def test_user_requires_password(app):
    from planteye.models.user import User
    user = User(password="hashed_pw")
    _db.session.add(user)
    with pytest.raises(IntegrityError):
        _db.session.commit()
    _db.session.rollback()

#TODO: test unhashed password

def test_user_requires_unique_email(app, user_data):
    from planteye.models.user import User
    dup = User(email="test@example.com", password="hashed_pw")
    _db.session.add(dup)
    with pytest.raises(IntegrityError):
        _db.session.commit()
    _db.session.rollback()

def test_plant_requires_name(app):
    from planteye.models.plant import Plant
    plant = Plant(desc="invalidplant")
    _db.session.add(plant)
    with pytest.raises(IntegrityError):
        _db.session.commit()
    _db.session.rollback()

def test_plant_sensor_requires_name(app):
    from planteye.models.plant_sensor import Plant_Sensor
    plant_sensor = Plant_Sensor(light_reading=45000.0)
    _db.session.add(plant_sensor)
    with pytest.raises(IntegrityError):
        _db.session.commit()
    _db.session.rollback()

def test_plant_sensor_requires_assoc(app):
    from planteye.models.plant_sensor import Plant_Sensor
    plant_sensor = Plant_Sensor(
            name="Mulberry Sensor",
            light_reading=45000.0,
            water_reading=0.6,
            soil=7.0
            )
    _db.session.add(plant_sensor)
    with pytest.raises(IntegrityError):
        _db.session.commit()
    _db.session.rollback()

def test_ai_output_requires_name(app):
    from planteye.models.ai_output
            )
    
