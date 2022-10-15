import os

import requests
from dotenv import load_dotenv
from simplejson import JSONDecodeError
from sklearn.linear_model import enet_path

load_dotenv()

API_ENDPOINT = "https://api.spotify.com/v1/me/player"

def __get_request_headers():
    access_token = os.getenv("access_token")
    if access_token != None:
        return {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + access_token
        }
    return ""

def get_devices():
    response = requests.get(url= API_ENDPOINT + "/devices", headers=__get_request_headers())
    if response.ok:
        devices = response.json().get("devices")
        for device in devices:
            print("_____________________________________")
            output = "Device name -- " + device["name"] \
                     + "\nDevice type -- " + device["type"] \
                     + "\nDevice ID -- " + device["id"]
            print(output)
            print("_____________________________________")
    else:
        print("Couldn't retrieve devices at this moment")

def search(keyword_type_list):
    keyword, type = keyword_type_list
    response = requests.get(url=f"https://api.spotify.com/v1/search?q={keyword}&type={type}", headers=__get_request_headers())
    if response.ok:
        data = response.json()
        for item in data.get(type+"s")["items"]:
            print(f"_________________________________")
            print("Name - {}".format(item.get("name")))
            print("Album - {}".format(item.get("album")["name"]))
            print("URI - {}".format(item.get("uri")))
            for serial_number, artist in enumerate(item.get("artists")):
                print(f"Artist {serial_number + 1} -- " + artist["name"])
            print(f"_________________________________")
    else:
        print("Couldn't perform search at this moment")

def get_currently_playing_song():
    response = requests.get(url=API_ENDPOINT + "/currently-playing", headers=__get_request_headers())
    data = None
    try:
        data = response.json()
    except JSONDecodeError:
        print("Either the device is offline, or no song is currently played")
    else:
        if response.ok and data:
            if data.get("item"):
                print("CURRENTLY PLAYING song: " + data["item"]["name"])
                for serial_number, artist in enumerate(data["item"].get("artists")):
                    print(f"Artist {serial_number + 1} -- " + artist["name"])
            else:
                print("CURRENTLY PLAYING an " + data["currently_playing_type"])
        else:
            print("Couldn't get currently playing song info")

def pause_currently_playing_song():
    response = requests.put(url=API_ENDPOINT + "/pause", headers=__get_request_headers())
    if response.ok:
        print("PAUSED the playback")
    else:
        print("FAILED to pause the playback")

def resume_currently_playing_song():
    response = requests.put(url=API_ENDPOINT + "/play", headers=__get_request_headers())
    if response.ok:
        print("RESUMED the playback")
    else:
        print("FAILED to resume the playback")

def play_next_song():
    response = requests.post(url=API_ENDPOINT + "/next", headers=__get_request_headers())
    if response.ok:
        print("PLAYING NEXT SONG")
    else:
        print("FAILED to play the next song")

def play_previous_song():
    response = requests.post(url=API_ENDPOINT + "/previous", headers=__get_request_headers())
    if response.ok:
        print("PLAYING PREVIOUS SONG")
    else:
        print("FAILED to play the previous song")

def adjust_volume(level):
    response = requests.put(url=API_ENDPOINT + f"/volume?volume_percent={level}", headers=__get_request_headers())
    if response.ok:
        print(f"VOLUME set to {level} percent")
    else:
        print("FAILED to set the volume")

def get_queue():
    response = requests.get(url=API_ENDPOINT + "/queue", headers=__get_request_headers())
    if response.ok:
        data = response.json()
        queue = data.get("queue")
        for object in queue:
            print(f"_________________________________")
            print("Name - {}".format(object.get("name")))
            print("Album - {}".format(object.get("album")["name"]))
            print("URI - {}".format(object.get("uri")))
            for serial_number, artist in enumerate(object.get("artists")):
                print(f"Artist {serial_number + 1} -- " + artist["name"])
            print(f"_________________________________",end="\n\n")
    else:
        print("FAILED to fetch user's queue")
