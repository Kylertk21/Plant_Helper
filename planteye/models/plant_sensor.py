from sqlalchemy import Integer, String, ForeignKey, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from planteye.db import db, Base

class Plant_Sensor(db.Model):
    __tablename__ = "plant_sensor"

    id: Mapped[int] = mapped_column(primary_key=True)
    plant_id: Mapped[int] = mapped_column(ForeignKey("plant.id"))
    type: Mapped[str] = mapped_column(String)
    name: Mapped[str] = mapped_column(String)
    light_reading: Mapped[float] = mapped_column(Float)
    water_reading: Mapped[float] = mapped_column(Float)
    soil: Mapped[float] = mapped_column(Float)

