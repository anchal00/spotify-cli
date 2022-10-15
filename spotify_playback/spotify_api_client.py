import os

import requests
from simplejson import JSONDecodeError

from spotify_playback.utils import (generic_error_message,
                                    map_http_status_to_reason)

API_ENDPOINT = "https://api.spotify.com/v1/me/player"

def __get_request_headers():
    access_token = os.getenv("access_token")
    if access_token != None:
        return {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + access_token
        }
    return ""

def api_call(path, method="get", endpoint=None, get_json=True):
    endpoint = endpoint or API_ENDPOINT
    response = requests.request(method=method, url= endpoint + path, headers=__get_request_headers())
    if response.ok:
        data = None
        if get_json:
            try:
                data = response.json()
                return (True, data)
            except JSONDecodeError:
                return (False, generic_error_message)
        return (True, data)
    else:
        return (False, map_http_status_to_reason(response.status_code))
