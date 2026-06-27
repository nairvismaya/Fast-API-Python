from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from urllib.parse import quote_plus

MYSQL_USER="root"
MYSQL_PASSWORD=quote_plus("Ilovedietcoke@2025")
MYSQL_HOST="localhost"
MYSQL_PORT=3306
MYSQL_DB="fastapi_db"

DATABASE_URL=f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"

##Connection
engine=create_engine(DATABASE_URL)

##Session
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:   
        db.close() 


##Base
Base=declarative_base() ## all the models will inherit from this base class
