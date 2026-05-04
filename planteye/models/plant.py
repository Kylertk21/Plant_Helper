from datetime import datetime
from sqlalchemy import DateTime, Text, String
from sqlalchemy.orm import Mapped, mapped_column
from planteye.db import db, Base

class Plant(db.Model):
    __tablename__ = "plant"

    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str] = mapped_column(String)
    scientific_name: Mapped[str] = mapped_column(String)
    name: Mapped[str] = mapped_column(String)
    desc: Mapped[str] = mapped_column(Text)
    link: Mapped[str] = mapped_column(unique=True)
    slug: Mapped[str] = mapped_column(unique=True)
    updated: Mapped[datetime] = mapped_column(DateTime)
    created: Mapped[datetime] = mapped_column(DateTime)
    growth: Mapped[str] = mapped_column(String)
    water: Mapped[str] = mapped_column(String)
    light: Mapped[str] = mapped_column(String)
    hardiness: Mapped[str] = mapped_column(String)
    soil: Mapped[str] = mapped_column(String)
    family: Mapped[str] = mapped_column(String)
