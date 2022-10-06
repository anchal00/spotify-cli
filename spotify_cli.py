import argparse
import sys

import auth
from playback import (adjust_volume, get_currently_playing_song,
                      pause_currently_playing_song)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Control spotify playback using your command line")
    subparser = parser.add_subparsers(help="Sub commands for controlling playback")

    # Auth controls
    parser.add_argument("--authenticate", help="Authorize with spotify APIs", action="store_true")

    # Playback controls
    playback_parser = subparser.add_parser(name="playback", description="Playback controls")
    playback_parser.add_argument("--current", help="Get currently playing song", action="store_true")
    playback_parser.add_argument("--playnext", help="Play next song", action="store_true")
    playback_parser.add_argument("--pause", help="Pause currently playing song", action="store_true")
    playback_parser.add_argument("--volume", help="Adjust the volume of currently playing song", type=int)

    args = parser.parse_args()
    print(args)
    if args.authenticate:
        is_successful = auth.authenticate()
        if is_successful == False:
            print("Error while completing authentication process")
            print("Exiting....")
            sys.exit()
    elif args.current:
        get_currently_playing_song()
    elif args.playnext:
        pass
    elif args.pause:
        pause_currently_playing_song()
    elif args.volume:
        adjust_volume(30)
