from sqlalchemy import Column, Integer,String,Boolean, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

#creating the base where I am going to create my table at.
base= declarative_base()

#creating a file where I am going to store my DataBase
engine= create_engine('SQLite///ArtistInfo.db')

#Creating my Table template.
class Table(base):
    __tablename__ = 'Artist Details'
    id = Column(Integer, primary_key=True)
    artist_name = Column(String(100))
    country = Column(String(100))
    featured = featuring= Column(Boolean)


#Populating my table with data given by the artist
artist_user = Table(artist_name= "Amour", country= "South Africa", featured= False, featuring= True)


#Locking my DataBase,making it recognisable and binding t to my session maker. 
base.metadata.create_all(engine)
Uploader=sessionmaker(bind=engine)

#Uploading the data to my DataBase
uploaded=Uploader().add(artist_user)