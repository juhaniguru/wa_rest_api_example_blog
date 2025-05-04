from sqlalchemy_utils import database_exists, create_database

import models
from db import engine

if not database_exists("sqlite:///blog.db"):
    create_database("sqlite:///blog.db")

models.Base.metadata.create_all(bind=engine)