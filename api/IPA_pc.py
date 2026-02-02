from fastapi import FastAPI
# from sqlalchemy import Column, String, Integer, create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base

""" Import Podcast As Pc """
# create a session and a Base 
# database = create_engine('Sqlite:///podcast_database.db', echo= True)
# upload = sessionmaker(database, bind=True)
# Base = declarative_base()
# # create Schema
# class Table(Base):
#     __tablename__ = 'Podcast_Database'
#     id = Column(Integer, primary_key=True)
#     name = Column(String, nullable= False)

# Base.metadata.create_all(upload)


 

# creating the app
app = FastAPI()

@app.get('/home')
def home_page(name: str = ''):
    welcome = {'name': {name}, 'text': f'Welcome {name} to Import Podcast As Pc'}
    # name = Table(name= name)
    return welcome if name.isalpha() else {'text':'Welcome to Import_Podcast_As_Pc'}
