import os
import sys

import spotipy
from dotenv import load_dotenv
from spotipy.exceptions import SpotifyException
from spotipy.oauth2 import SpotifyOAuth

from utils import print_album_info, print_playlist_info, print_track_info

REDIRECT_URI = "http://localhost:8000/callback"

class SpotifyClient:

    _scopes = [
        "user-read-private",
        "user-read-email",
        "user-modify-playback-state",
        "user-read-currently-playing",
        "user-read-playback-state"
    ]

    def __init__(self):
        load_dotenv(".env")
        self.auth_manager = SpotifyOAuth(scope=self._scopes,
                                         client_id=os.getenv("client_id"),
                                         client_secret=os.getenv("client_secret"),
                                         redirect_uri=REDIRECT_URI)

    def __get_client(self):
        token = self.auth_manager.get_cached_token()
        if not token:
            print("Please authenticate with Spotify first")
            sys.exit()
        self.auth_manager.validate_token(token)
        return spotipy.Spotify(auth=self.auth_manager.get_cached_token()["access_token"])

    def authenticate(self):
        self.auth_manager.get_access_token()
        spotipy.Spotify(auth_manager=self.auth_manager)
        print("Authentication Successful")

    def get_devices(self):
        result = self.__get_client().devices()
        if result is None:
            print(f"Couldn't retrieve devices at this moment")
            return
        for device in result.get("devices", []):
                print("_____________________________________")
                output = "Device name -- " + device["name"] \
                        + "\nDevice type -- " + device["type"] \
                        + "\nDevice ID -- " + device["id"]
                print(output)
                print("_____________________________________")

    def search(self, keyword_type_list):
        keyword, type = keyword_type_list
        result = self.__get_client().search(keyword, type=type)
        if not result:
            print("Couldn't perform the search at this moment.")
            return
        for item in result.get(type+"s").get("items", []):
            if type == "track":
                print_track_info(item)
            elif type == "album":
                print_album_info(item)
            elif type == "playlist":
                print_playlist_info(item)            
        else:
            print(f"Couldn't perform the search. Please check the command")

    def get_currently_playing_song(self):
        data = self.__get_client().current_user_playing_track()
        if data:
            if data.get("item"):
                print_track_info(data["item"])
            else:
                print("CURRENTLY PLAYING an " + data["currently_playing_type"])
        else:
            print(f"Couldn't get currently playing song info")

    def pause_currently_playing_song(self):
        data = self.__get_client().pause_playback()
        if data:
            print("PAUSED the playback")
        else:
            print(f"FAILED to pause the playback")

    def resume_currently_playing_song(self):
        data = self.__get_client().start_playback()
        if data:
            print("RESUMED the playback")
        else:
            print(f"FAILED to resume the playback")

    def play_next_song(self):
        try:
            self.__get_client().next_track()
            print("PLAYING next song")
            self.get_currently_playing_song()
        except SpotifyException:
            print(f"FAILED to play the next song")

    def play_previous_song(self):
        try:
            self.__get_client().previous_track()
            print("PLAYING previous song")
            self.get_currently_playing_song()
        except SpotifyException:
            print(f"FAILED to play the previous song")

    def adjust_volume(self, level):
        # Fix
        data = self.__get_client().volume(level)
        if data:
            print(f"VOLUME set to {level} percent")
        else:
            print(f"FAILED to set the volume")

    def get_queue(self):
        data = self.__get_client().queue()
        if data:
            for object in data.get("queue", []):
                print_track_info(object)
        else:
            print(f"FAILED to fetch user's queue")

    def add_to_queue(self, uri):
        data = self.__get_client().add_to_queue(uri)
        if data:
            print("Item added to the queue")
        else:
            print(f"FAILED to add the item to the queue")
