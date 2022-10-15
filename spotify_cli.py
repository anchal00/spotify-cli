import argparse
import os
import sys

from dotenv import load_dotenv

import auth
from playback import (adjust_volume, get_currently_playing_song, get_devices,
                      get_queue, pause_currently_playing_song, play_next_song,
                      play_previous_song, resume_currently_playing_song,
                      search)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Control spotify playback using your command line")
    subparser = parser.add_subparsers(help="Sub commands for controlling playback")
    # Auth controls
    parser.add_argument("--authenticate", help="Authorize with spotify APIs", action="store_true")
    # Playback controls
    playback_parser = subparser.add_parser(name="playback", description="Playback controls")
    playback_parser.add_argument("--current", help="Get currently playing song", action="store_true")
    playback_parser.add_argument("--next", help="Play next song", action="store_true")
    playback_parser.add_argument("--prev", help="Play previous song", action="store_true")
    playback_parser.add_argument("--resume", help="Resume the currently playing song", action="store_true")
    playback_parser.add_argument("--pause", help="Pause currently playing song", action="store_true")
    playback_parser.add_argument("--volume", help="Adjust the volume of currently playing song", type=int)
    playback_parser.add_argument("--search", help="Search for a song", type=str, nargs='+')
    playback_parser.add_argument("--devices", help="Get all your devices", action="store_true")
    playback_parser.add_argument("--queue", help="Get user's queue", action="store_true")
    args = parser.parse_args()

    if not os.path.isfile(".env"):
        print("Please create .env file in current dir before proceeding")
        sys.exit()

    if args.authenticate:
        is_successful = auth.authenticate()
        if is_successful == False:
            print("Error while completing authentication process")
            print("Exiting....")
            sys.exit()
    elif args.current:
        get_currently_playing_song()
    elif args.resume:
        resume_currently_playing_song()
    elif args.next:
        play_next_song()
    elif args.prev:
        play_previous_song()
    elif args.pause:
        pause_currently_playing_song()
    elif args.volume:
        adjust_volume(args.volume)
    elif args.search:
        search(args.search)
    elif args.devices:
        get_devices()
    elif args.queue:
        get_queue()
