import dbmanagement
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

class Inventory(dbmanagement.Base):
    """Associate a character with a list of item"""
    __tablename__ = 'inventory'
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('character.id'))
    character = relationship('Character')
    item_id = relationship("Item")
    quantity = Column(Integer, default=0)