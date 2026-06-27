from database import engine,Base
import model ## import all the models defined in model.py

Base.metadata.create_all(bind=engine) ## create all the tables in the database based on the models defined in model.py
