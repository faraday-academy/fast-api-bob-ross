from sqlalchemy import Column, ForeignKey, Integer, Text, String, Table
from sqlalchemy.orm import relationship

from ..db_setup import Base

episodes_quotes = Table(
    "episodes_quotes",
    Base.metadata,
    Column("episode_id", ForeignKey("episodes.id"), primary_key=True),
    Column("quote_id", ForeignKey("quotes.id"), primary_key=True),
)

episodes_guests = Table(
    "episodes_guests",
    Base.metadata,
    Column("episode_id", ForeignKey("episodes.id"), primary_key=True),
    Column("guest_id", ForeignKey("guests.id"), primary_key=True),
)

episodes_animals = Table(
    "episodes_animals",
    Base.metadata,
    Column("episode_id", ForeignKey("episodes.id"), primary_key=True),
    Column("animal_id", ForeignKey("animals.id"), primary_key=True),
)


class Quote(Base):
    __tablename__ = "quotes"

    id = Column(Integer, primary_key=True)
    text = Column(Text, nullable=False)

    episodes = relationship(
        "Episode", secondary=episodes_quotes, back_populates="quotes"
    )


class Guest(Base):
    __tablename__ = "guests"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    episodes = relationship(
        "Episode", secondary=episodes_guests, back_populates="guests"
    )


class Animal(Base):
    __tablename__ = "animals"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)
    species = Column(String, nullable=False)

    episodes = relationship(
        "Episode", secondary=episodes_animals, back_populates="animals"
    )
