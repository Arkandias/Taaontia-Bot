import dbmanagement
from sqlalchemy import Column, ForeignKey, Integer, String

class Item(dbmanagement.Base):
    """Defines an item attributes"""
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    type = Column(Integer, nullable=False)
    level = Column(Integer, nullable=False)