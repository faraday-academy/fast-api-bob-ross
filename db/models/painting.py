import enum

from sqlalchemy import Column, ForeignKey, Integer, String, Enum, Table
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Unicode

from ..db_setup import Base


class PaintingType(enum.IntEnum):
    landscape = 1
    portrait = 2


paintings_colors = Table(
    "paintings_colors",
    Base.metadata,
    Column("painting_id", ForeignKey("paintings.id"), primary_key=True),
    Column("paint_color_id", ForeignKey("paint_colors.id"), primary_key=True),
)


class Painting(Base):
    __tablename__ = "paintings"

    id = Column(Integer, primary_key=True)
    episode_id = Column(Integer, ForeignKey("episodes.id"), nullable=False)
    title = Column(String(100), nullable=False)
    image_url = Column(String, nullable=True)
    type = Column(Enum(PaintingType))

    # TODO: many to many episode_references
    episode = relationship("Episode", back_populates="painting", uselist=False)
    paint_colors = relationship(
        "PaintColor", secondary=paintings_colors, back_populates="paintings"
    )


class PaintColor(Base):
    __tablename__ = "paint_colors"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    hex = Column(String, nullable=False)

    paintings = relationship(
        "Paintings", secondary=paintings_colors, back_populates="paint_colors"
    )
