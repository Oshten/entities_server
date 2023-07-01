from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Entity(Base):
    """Model for entities"""
    __tablename__ = 'entities'
    id = Column(Integer, primary_key=True)
    name = Column(String(36), unique=True)
    created_at = Column(DateTime(), default=datetime.now)

    def __str__(self):
        return f'{self.id}. Entity {self.name}, created at {datetime.strftime(self.created_at, "%d.%m.%y %H:%M")}'

    def __repr__(self):
        return str(self)
