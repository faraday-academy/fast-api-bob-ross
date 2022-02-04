# painting and paintcolor
from sqlalchemy import Column, ForeignKey, Integer, String, null
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Unicode

from ..db_setup import Base


class Painting(Base):
    __tablename__ = "paintings"

    id = Column(Integer, primary_key=True)
    episode_id = Column(Integer, ForeignKey("seasons.id"), nullable=False)
    title = Column(String(100), nullable=False)
    image_url = Column(String, nullable=True)
    type = Column(String(25), nullable=False)

    # TODO: many to many episode_references
    # season = relationship("Season", back_populates="episodes")


class PaintColor(Base):
    __tablename__ = "paint_colors"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    hex = Column(String, nullable=False)
    # TODO: paintings = m2m with paintings
