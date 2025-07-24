import os
import time
import pandas as pd
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import json

# Cargar variables de entorno desde .env
load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")
SCOPE = "user-read-playback-state user-read-currently-playing user-modify-playback-state"

# Autenticación con Spotipy
sp = Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=SCOPE,
    open_browser=True
))

def get_artist_popularity(artist_name):
    results = sp.search(q=f'artist:"{artist_name}"', type='artist', limit=5)
    items = results['artists']['items']
    for artist in items:
        if artist['name'].lower() == artist_name.lower():
            return {
                'name': artist['name'],
                'id': artist['id'],
                'popularity': artist['popularity']
            }
    return None


artist1 = get_artist_popularity("Luca Sestak")
artist2 = get_artist_popularity("Mathieu Fiset")

if artist1 and artist2:
    diff = abs(artist1['popularity'] - artist2['popularity'])
    print(f"{artist1['name']} tiene popularidad {artist1['popularity']}")
    print(f"{artist2['name']} tiene popularidad {artist2['popularity']}")
    print(f"Diferencia de popularidad: {diff}")
else:
    print("No se pudo encontrar uno de los artistas")
