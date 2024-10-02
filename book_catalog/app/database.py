from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = "postgresql://ashwindb_avvw_user:T4iasgf7j2sHodcA32DkTve4mmt4uWmC@dpg-crts9e8gph6c73dara10-a.oregon-postgres.render.com/ashwindb_avvw" #os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
