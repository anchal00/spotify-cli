import base64
import os

import requests
from dotenv import load_dotenv

authentication_url = "https://accounts.spotify.com/api/token"

load_dotenv()

client_id = os.getenv("client_id")
client_secret  = os.getenv("client_secret")

headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Authorization": "Basic " 
                     + base64.b64encode((client_id + ":" + client_secret).encode("ascii")).decode("ascii")
}

def authenticate():
    response = requests.post(url=authentication_url, 
                             params={"grant_type": "client_credentials"}, headers=headers)
    if response.ok:
        data = response.json()
        return (True, data["access_token"])
    return (False, "")

