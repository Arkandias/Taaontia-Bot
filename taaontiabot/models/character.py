import dbmanagement
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Character(dbmanagement.Base):
	"""Defines a character's attributes"""
	__tablename__= 'character'
	id = Column(Integer, primary_key=True)
	name = Column(String(30), nullable=False)
	level = Column(Integer, default=1)
	experience = Column(Integer, default=0)
	inventory = relationship("Inventory")