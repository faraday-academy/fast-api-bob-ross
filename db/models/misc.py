from sqlalchemy import Column, ForeignKey, Integer, Text, String
from sqlalchemy.orm import relationship

from ..db_setup import Base


class Quote(Base):
    __tablename__ = "quotes"

    id = Column(Integer, primary_key=True)
    text = Column(Text, nullable=False)

    # TODO: many to many episodes


class Guest(Base):
    __tablename__ = "guests"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    # TODO: many to many episodes


class Animal(Base):
    __tablename__ = "animals"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)
    species = Column(String, nullable=False)
    # TODO: m2m with episodes
