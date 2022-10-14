import base64
import os
import webbrowser

import requests
from dotenv import load_dotenv, set_key

AUTH_URL = "https://accounts.spotify.com"
REDIRECT_URI = "http://localhost:8000/callback"

load_dotenv()

client_id = os.getenv("client_id")
client_secret  = os.getenv("client_secret")

scopes = [
    "user-read-private",
    "user-read-email",
    "user-modify-playback-state",
    "user-read-currently-playing",
    "user-read-playback-state"
]

def __get_request_headers():
    return {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": "Basic " 
                        + base64.b64encode((client_id + ":" + client_secret).encode("ascii")).decode("ascii")
    }

def authenticate():
    scope_str = " ".join(scopes)
    response = requests.get(f'{AUTH_URL}/authorize?client_id={client_id}&scope={scope_str}&response_type=code&redirect_uri={REDIRECT_URI}')
    webbrowser.open(response.url)
    code = input("""Grant the access to spotify-cli and Enter the code from the url 
                 \ne.g. If the address shown in the browser's address bar is -> http://localhost:8000/callback?code=abcdef then abcdef is the code that you need to enter: """)
    response = requests.post(url=f"{AUTH_URL}/api/token", 
                             params={"grant_type": "authorization_code", "code": code, "redirect_uri": REDIRECT_URI}, headers=__get_request_headers())
    if response.ok:
        data = response.json()
        set_key(dotenv_path= os.getcwd() + '/.env', key_to_set="access_token", value_to_set=data["access_token"])
        set_key(dotenv_path= os.getcwd() + '/.env', key_to_set="refresh_token", value_to_set=data["refresh_token"])
        # Todo : Add support for using refresh tokens
        return True
    return False

