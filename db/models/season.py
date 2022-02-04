from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship

from ..db_setup import Base


class Season(Base):
    __tablename__ = "seasons"

    id = Column(Integer, primary_key=True)
    number = Column(Integer, unique=True)
    year = Column(Integer, nullable=False)

    episodes = relationship("Episode", back_populates="season")
