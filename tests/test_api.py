import uuid
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient

from app.server import app
from app import route
from database.models import Base, Entity
from docs.config import TEST_DATABASE_URL


engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
Base.metadata.create_all(bind=engine)
TestSession = sessionmaker(bind=engine)

route.Session = TestSession
client = TestClient(app)

some_entity = {'entity': str(uuid.uuid4())}

def test_query_all_entities():
    assert client.get('/api/entities').status_code == 200

def test_add_entity():
    response = client.post('/api/entities', json=some_entity)
    assert response.status_code == 201
    assert response.json() == {'message': f'Entity {some_entity["entity"]} created'}

def test_repeated_add_entity():
    response = client.post('/api/entities', json=some_entity)
    assert response.status_code == 400
    assert response.json() == {'error': f'Entity {some_entity["entity"]} exist.'}

def test_attempt_wrong_add_entity():
    response = client.post('/api/entities', json={})
    assert response.status_code == 400
    assert response.json() == {'error': 'Does not specified name entity'}