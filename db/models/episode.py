from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import null
from sqlalchemy.sql.sqltypes import Unicode

from ..db_setup import Base


class Episode(Base):
    __tablename__ = "episodes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    season = Column(Integer, nullable=False)
    description = Column(Unicode, nullable=True)
    date = Column(String(25), nullable=False)
