from sqlalchemy import Column,String,Integer, create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from fastapi import FastAPI
# from pydantic import BaseModel
# import pandas

#Creating a database file enviroment
engine= create_engine('sqlite:///artist_songs.db')
base= declarative_base()

#Creating a sessionmaker and binding the engine to be able to send data
uploader= sessionmaker(bind=engine)

#Creating the table column and name
class Table(base):
    __tablename__ = 'ArtistSongs'
    id= Column(Integer, primary_key=True)
    artist_name= Column(String)
    song_title= Column(String)
    country= Column(String)
    year= Column(Integer)

    @property
    def info(self):
        return {
            'id': self.id,
            'artist_name': self.artist_name,
            'song_title': self.song_title,
            'country': self.country,
            'year': self.year
        }

#Registering my engine
base.metadata.create_all(engine)

#Storing data
artist_songs = Table(artist_name='Amour', 
                     song_title='Sbali',
                     country='South Africa',
                     year=2025)

#Creating a Dataframe using the database
# data= pandas.DataFrame(artist_songs)

'''FastApi to create api for the arist data'''
app= FastAPI()

@app.get('/artist_songs')
def read():
    return artist_songs.info

@app.post('/artist_songs')
def create(artist_name:str,song_title:str,country:str = 'World',year:int = None):
    artist_name +=  Table(artist_name=artist_name, 
                     song_title=song_title,
                     country=country,
                     year=year)

#Binding and adding the data to the engine
upload= uploader()
upload.add(artist_songs)
upload.commit()


