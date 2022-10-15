import os

import requests
from dotenv import load_dotenv
from simplejson import JSONDecodeError

load_dotenv()

API_ENDPOINT = "https://api.spotify.com/v1/me/player"

generic_error_message = "Couldn't complete the request. Something went wrong"

status_to_reason_map = {
        401: "Bad or expired token. Please re-authenticate yourself",
        403: "Bad request",
        409: "Request Limit Exceeded. Cannot handle any further requests"
    }

def __get_request_headers():
    access_token = os.getenv("access_token")
    if access_token != None:
        return {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + access_token
        }
    return ""

def print_track_info(track):
    print(f"_________________________________")
    print("Name - {}".format(track.get("name")))
    print("Album - {}".format(track.get("album")["name"]))
    print("URI - {}".format(track.get("uri")))
    for serial_number, artist in enumerate(track.get("artists")):
        print(f"Artist {serial_number + 1} -- " + artist["name"])
    print(f"_________________________________",end="\n\n")

def __api_call(path, method="get", endpoint=None, get_json=True):
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
        status_code = response.status_code
        reason = status_to_reason_map.get(status_code) if status_code in status_to_reason_map else generic_error_message
        return (False, reason)

def get_devices():
    is_ok, data = __api_call("/devices")
    if is_ok:
        devices = data.get("devices")
        for device in devices:
            print("_____________________________________")
            output = "Device name -- " + device["name"] \
                     + "\nDevice type -- " + device["type"] \
                     + "\nDevice ID -- " + device["id"]
            print(output)
            print("_____________________________________")
    else:
        print(f"Couldn't retrieve devices at this moment : Reason - {data}")

def search(keyword_type_list):
    keyword, type = keyword_type_list
    is_ok, data = __api_call(path=f"/search?q={keyword}&type={type}", endpoint="https://api.spotify.com/v1")
    if is_ok:
        for item in data.get(type+"s")["items"]:
           print_track_info(item)
    else:
        print(f"Couldn't perform search at this moment : Reason - {data}")

def get_currently_playing_song():
    is_ok, data = __api_call(path="/currently-playing")
    if is_ok:
        if data.get("item"):
            print_track_info(data["item"])
        else:
            print("CURRENTLY PLAYING an " + data["currently_playing_type"])
    else:
        print(f"Couldn't get currently playing song info : Reason - {data}")

def pause_currently_playing_song():
    is_ok, data = __api_call(path="/pause", method="put", get_json=False)
    if is_ok:
        print("PAUSED the playback")
    else:
        print(f"FAILED to pause the playback : Reason - {data}")

def resume_currently_playing_song():
    is_ok, data = __api_call(path="/play", method="put", get_json=False)
    if is_ok:
        print("RESUMED the playback")
    else:
        print(f"FAILED to resume the playback : Reason - {data}")

def play_next_song():
    is_ok, data = __api_call(path="/next", method="post", get_json=False)
    if is_ok:
        print("PLAYING next song")
        get_currently_playing_song()
    else:
        print(f"FAILED to play the next song : Reason - {data}")

def play_previous_song():
    is_ok, data = __api_call(path="/previous", method="post", get_json=False)
    if is_ok:
        print("PLAYING previous song")
        get_currently_playing_song()
    else:
        print(f"FAILED to play the previous song : Reason - {data}")

def adjust_volume(level):
    is_ok, data = __api_call(path=f"/volume?volume_percent={level}", method="put")
    if is_ok:
        print(f"VOLUME set to {level} percent")
    else:
        print(f"FAILED to set the volume : Reason - {data}")

def get_queue():
    is_ok, data = __api_call(path= "/queue")
    if is_ok:
        queue = data.get("queue")
        for object in queue:
            print_track_info(object)
    else:
        print(f"FAILED to fetch user's queue: Reason - {data}")
