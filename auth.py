import base64
import os
import webbrowser

import requests
from dotenv import load_dotenv

AUTH_URL = "https://accounts.spotify.com"

load_dotenv()

code = None
client_id = os.getenv("client_id")
client_secret  = os.getenv("client_secret")

REDIRECT_URI = "http://localhost:8000/callback"
scopes = ["user-read-private", "user-read-email", "user-modify-playback-state"]

headers = {
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
                             params={"grant_type": "authorization_code", "code": code, "redirect_uri": REDIRECT_URI}, headers=headers)
    if response.ok:
        data = response.json()
        return (True, data["access_token"])
    return (False, "")

