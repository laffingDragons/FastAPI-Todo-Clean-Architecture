from fastapi import FastAPI
from .database.core import engine, Base
from .entities.todo import Todo #Import model to register them
from .entities.user import User #Import model to register them
from .api import register_routes

app = FastAPI()

''' 
Only uncomment below to create new tables otherwise test cases will fail
'''

#Base.metadata.create_all(bind=engine)