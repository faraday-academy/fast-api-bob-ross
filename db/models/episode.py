from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Unicode

from ..db_setup import Base


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
