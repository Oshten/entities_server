from sqlalchemy.orm import Session

from database.models import Entity

class DatabaseIteraction:
    """Class for interacting with the database using models"""

    def __init__(self, session: Session):
        self.session = session

    def select_all(self):
        entities = self.session.query(Entity).all()
        return entities

    def create_new_entity(self, name_entity):
        new_entity = Entity(name=name_entity)
        self.session.add(new_entity)
        self.session.commit()


def insert_new_entity(name: str):
    """Insert to database new entity"""
    session = Session()
