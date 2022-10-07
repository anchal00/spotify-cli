import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_ENDPOINT = "https://api.spotify.com/v1/me/player"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + os.getenv("access_token")
}

def get_currently_playing_song():
    response = requests.get(url=API_ENDPOINT + "/currently-playing", headers=headers)
    data = response.json()
    if response.ok and data:
        if data.get("item"):
            print("CURRENTLY PLAYING song: " + data["item"]["name"])
        else:
            print("CURRENTLY PLAYING an " + data["currently_playing_type"])
    else:
        print("Couldn't get currently playing song info")

def pause_currently_playing_song():
    response = requests.put(url=API_ENDPOINT + "/pause", headers=headers)
    if response.ok:
        print("PAUSED the playback")
    else:
        print("FAILED to pause the playback")

def resume_currently_playing_song():
    response = requests.put(url=API_ENDPOINT + "/play", headers=headers)
    if response.ok:
        print("RESUMED the playback")
    else:
        print("FAILED to resume the playback")

def play_next_song():
    response = requests.post(url=API_ENDPOINT + "/next", headers=headers)
    if response.ok:
        print("PLAYING NEXT SONG")
    else:
        print("FAILED to play the next song")

def play_previous_song():
    response = requests.post(url=API_ENDPOINT + "/previous", headers=headers)
    if response.ok:
        print("PLAYING PREVIOUS SONG")
    else:
        print("FAILED to play the previous song")

def adjust_volume(level):
    response = requests.put(url=API_ENDPOINT + f"/volume?volume_percent={level}", headers=headers)
    if response.ok:
        print(f"VOLUME set to {level} percent")
    else:
        print("FAILED to set the volume")
