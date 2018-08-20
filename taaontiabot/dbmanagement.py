from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

Base = declarative_base()
engine = create_engine('sqlite:///:memory:', echo=True)

def setup_db():
    """Creating / Connecting to DB"""
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    setup_db()