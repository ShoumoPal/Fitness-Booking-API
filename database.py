# Module to initialize the database (SQLite)

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Loading environment variables
load_dotenv(override=True)

# DB url
SQLITE_URL = os.getenv('SQLITE_URL')

# Initializing connection
engine = create_engine(SQLITE_URL, connect_args={'check_same_thread' : False})
LocalSession = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()