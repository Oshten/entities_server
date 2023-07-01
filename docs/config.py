import os
import sys
import logging

from starlette.config import Config

# -- Project information -----------------------------------------------------

project = "Entities server"
author = "Oshten"

# -- Configuration settings -----------------------------------------------------

ROOT_DIR_NAME = os.path.abspath('..')
sys.path.insert(0, ROOT_DIR_NAME)
config = Config(f'{ROOT_DIR_NAME}/.env')


#Configuration postgre
DB_HOST = 'postgres'
DB_PORT = 5432
DB_USERNAME = config('POSTGRES_USER', cast=str, default='user')
DB_PASSWORD = config('POSTGRES_PASSWORD', cast=str, default='12345')
DB_NAME = config('POSTGRES_DB', cast=str, default='entities')
DATABASE_URL = f'postgresql+psycopg2://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
TEST_DATABASE_URL = "sqlite:///test_entities.db"



