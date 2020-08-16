import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

class Room:
    def __init__(self, id, artist):
        self.players = []
        self.artist = artist
        self.songs = self.get_songs(artist)
        self.id = id
    
    def get_songs(self, artist):
        auth_manager = SpotifyClientCredentials()
        sp = spotipy.Spotify(auth_manager=auth_manager)
        results = sp.search(q=artist, type='track', limit=8)
        print(results)


r = Room(32, 'tyler the creator')