from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Unicode

from ..db_setup import Base
from .misc import episodes_quotes, episodes_guests, episodes_animals


class Episode(Base):
    __tablename__ = "episodes"

    id = Column(Integer, primary_key=True)
    season_id = Column(Integer, ForeignKey("seasons.id"), nullable=False)
    number = Column(Integer, nullable=False)
    title = Column(String(100), nullable=False)
    description = Column(Unicode, nullable=True)
    youtube_url = Column(String, nullable=True)
    date = Column(String(25), nullable=False)

    season = relationship("Season", back_populates="episodes")
    painting = relationship("Painting", back_populates="episode")

    quotes = relationship(
        "Quote", secondary=episodes_quotes, back_populates="episodes"
    )
    guests = relationship(
        "Guest", secondary=episodes_guests, back_populates="episodes"
    )
    animals = relationship(
        "Animal", secondary=episodes_animals, back_populates="episodes"
    )
