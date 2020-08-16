"""
some code based off of https://github.com/vanortg/Flask-Spotify-Auth
"""

from flask import Flask, redirect, request
import requests

app = Flask(__name__)

SPOTIFY_URL_AUTH = "https://accounts.spotify.com/authorize?"
SPOTIFY_URL_TOKEN = "https://accounts.spotify.com/api/token"
RESPONSE_TYPE = "code"
SCOPE = "streaming"  # change this to whatever is required
CLIENT_ID = "1615209a464c4661b5fb11029a5d7b5b"
CLIENT_SECRET = 4  # secret goes here


def authQuery(redirect_uri):
    return SPOTIFY_URL_AUTH + "client_id={}&response_type={}&redirect_uri={}&scope={}".format(CLIENT_ID, RESPONSE_TYPE, redirect_uri, SCOPE)


"""
def tokenQuery(redirect_uri):
    body = {

    }
    return SPOTIFY_URL_TOKEN + "client_id={}&client_secret={}&grant_type={}&code={}&redirect_uri".format(CLIENT_ID, CLIENT_SECRET, redirect_uri, SCOPE)
"""


@app.route('/')
def hello_world():
    return 'Hello, world'


@app.route('/auth/', methods=["GET", "POST"])
def authenticate():
    return redirect(authQuery("http://localhost:5000/authLog/"))


@app.route('/authLog/', methods=["GET", "POST"])
def authLog():
    code = request.args.get('code', type = str)

    if "error" in code:
        return redirect("/authFail")

    body = {"grant_type": "authorization code",
            "code": code,
            "redirect_uri": "http://localhost:5000/authLog",
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET
            }

    #  requests.post(SPOTIFY_URL_TOKEN, grant_type="authorization_code", , redirect_uri="http://localhost:5000/authLog", client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
    requests.post(SPOTIFY_URL_TOKEN, data=body)

    return redirect("/authSuccess")


@app.route('/authSuccess/')
def authSuccess():
    return "congrats, you have logged into spotify"


@app.route('/authFail/')
def authFail():
    return "unfortunately, you have not logged into spotify"
