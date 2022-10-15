import os

from dotenv import load_dotenv

from spotify_playback.spotify_api_client import api_call
from spotify_playback.utils import print_album_info, print_track_info

load_dotenv()

def get_devices():
    is_ok, data = api_call("/devices")
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
    is_ok, data = api_call(path=f"/search?q={keyword}&type={type}", endpoint="https://api.spotify.com/v1")
    if is_ok:
        for item in data.get(type+"s")["items"]:
            if type == "track":
                print_track_info(item)
            elif type == "album":
                print_album_info(item)
    else:
        print(f"Couldn't perform search at this moment : Reason - {data}")

def get_currently_playing_song():
    is_ok, data = api_call(path="/currently-playing")
    if is_ok:
        if data.get("item"):
            print_track_info(data["item"])
        else:
            print("CURRENTLY PLAYING an " + data["currently_playing_type"])
    else:
        print(f"Couldn't get currently playing song info : Reason - {data}")

def pause_currently_playing_song():
    is_ok, data = api_call(path="/pause", method="put", get_json=False)
    if is_ok:
        print("PAUSED the playback")
    else:
        print(f"FAILED to pause the playback : Reason - {data}")

def resume_currently_playing_song():
    is_ok, data = api_call(path="/play", method="put", get_json=False)
    if is_ok:
        print("RESUMED the playback")
    else:
        print(f"FAILED to resume the playback : Reason - {data}")

def play_next_song():
    is_ok, data = api_call(path="/next", method="post", get_json=False)
    if is_ok:
        print("PLAYING next song")
        get_currently_playing_song()
    else:
        print(f"FAILED to play the next song : Reason - {data}")

def play_previous_song():
    is_ok, data = api_call(path="/previous", method="post", get_json=False)
    if is_ok:
        print("PLAYING previous song")
        get_currently_playing_song()
    else:
        print(f"FAILED to play the previous song : Reason - {data}")

def adjust_volume(level):
    is_ok, data = api_call(path=f"/volume?volume_percent={level}", method="put")
    if is_ok:
        print(f"VOLUME set to {level} percent")
    else:
        print(f"FAILED to set the volume : Reason - {data}")

def get_queue():
    is_ok, data = api_call(path= "/queue")
    if is_ok:
        queue = data.get("queue")
        for object in queue:
            print_track_info(object)
    else:
        print(f"FAILED to fetch user's queue: Reason - {data}")
