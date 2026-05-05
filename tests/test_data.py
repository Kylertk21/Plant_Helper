import pytest
from planteye.db import db

def test_user_created(app, user_data):
    from planteye.models.user import User
    user = User.query.first()
    assert user is not None
    assert user.email == "test@example.com"

    # TODO: test password hashed

def test_plant_created(app, plant_data):
    from planteye.models.plant import Plant
    plant = Plant.query.first()
    assert plant is not None
    assert plant.name == "White mulberry"

def test_plant_sensor_created(app, plant_sensor_data):
    from planteye.models.plant_sensor import Plant_Sensor
    plant_sensor = Plant_Sensor.query.first()
    assert plant_sensor is not None
    assert plant_sensor.name == "Mulberry Sensor"

def test_ai_output_created(app, ai_output):
    from planteye.models.ai_output import Ai_Output
    ai_output = Ai_Output.query.first()
    assert ai_output is not None
    assert ai_output.severity == "Medium"
