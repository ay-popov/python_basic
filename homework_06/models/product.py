from sqlalchemy import Column, Integer, String
from .database import db


class Product(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True, nullable=False)
    Text = Column(String(500), unique=False, nullable=True)
