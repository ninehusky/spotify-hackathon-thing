"""
code based off of https://github.com/vanortg/Flask-Spotify-Auth
"""


from flask import Flask, redirect
import spotipy
from spotipy.oauth2 import SpotifyOAuth


app = Flask(__name__)

SPOTIFY_URL_AUTH = "https://accounts.spotify.com/authorize?"
SPOTIFY_URL_TOKEN = "https://accounts.spotify.com/api/token"
RESPONSE_TYPE = "code"
SCOPE = "streaming"  # change this to whatever is required
CLIENT_ID = "1615209a464c4661b5fb11029a5d7b5b"


def authQuery(redirect_uri):
    return SPOTIFY_URL_AUTH + "client_id={}&response_type={}&redirect_uri={}&scope={}".format(CLIENT_ID, RESPONSE_TYPE, redirect_uri, SCOPE)


"""
def getUser():
    return getAuth(CLIENT_ID, RESPONSE_TYPE, "https://localhost/5000/", SCOPE)
"""


@app.route('/')
def hello_world():
    return 'Hello, world'


@app.route('/auth/', methods=['GET', 'POST'])
def authenticate():
    return redirect(authQuery("http://localhost:5000/authLog/"))


@app.route('/authLog/')
def authLog():
    return redirect("/authFail")


@app.route('/authSuccess/')
def authSuccess():
    return "congrats, you have logged into spotify"


@app.route('/authFail/')
def authFail():
    return "unfortunately, you have not logged into spotify"