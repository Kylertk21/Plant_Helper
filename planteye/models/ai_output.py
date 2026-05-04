from datetime import datetime
from sqlalchemy import Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from planteye.db import db, Base

class Ai_Output(db.Model):
    __tablename__ = "ai_output"

    id: Mapped[int] = mapped_column(primary_key=True)
    plant_id: Mapped[int] = mapped_column(ForeignKey("plant.id"))
    created: Mapped[datetime] = mapped_column(DateTime)
    severity: Mapped[str] = mapped_column(String)
    message: Mapped[str] = mapped_column(Text)
