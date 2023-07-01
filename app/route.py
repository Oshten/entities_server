import datetime

from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database.scripts import DatabaseIteraction
from docs.config import DATABASE_URL


router = APIRouter()

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

@router.get('/api/entities')
def get_entities():
    """Get list all entities from database"""
    with Session() as session:
        db = DatabaseIteraction(session)
        entities = db.select_all()
    return entities


@router.post('/api/entities', status_code=201)
def create_entity(content=Body(default={})):
    """Insert new entity to database"""
    name = content.get('entity')
    if name:
        try:
            with Session() as session:
                db = DatabaseIteraction(session)
                db.create_new_entity(name)
            return {'message': f'Entity {name} created'}

        except Exception as exc:
            resource = JSONResponse(content={'error': f'Entity {name} exist.'})
    else:
        resource = JSONResponse(content={'error': 'Does not specified name entity'})

    resource.status_code = 400
    return resource
