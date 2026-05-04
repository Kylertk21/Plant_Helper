from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from planteye.db import db


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str] = mapped_column #TODO: Hash password


