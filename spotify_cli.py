import argparse
import os
import sys

from spotify_playback.spotify_client import SpotifyClient

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Control spotify playback using your command line", add_help=False
    )
    subparser = parser.add_subparsers(help="Sub commands for controlling playback")
    # Auth controls
    parser.add_argument("-auth", help="Authorize with spotify APIs", action="store_true")
    parser.add_argument("-h", help="Help", action="store_true")
    # Playback controls
    playback_parser = subparser.add_parser(name="playback", description="Playback controls", add_help=True)
    playback_parser.add_argument("-cr", help="Get currently playing song", action="store_true")
    playback_parser.add_argument("-ppr", help="Play previous song", action="store_true")
    playback_parser.add_argument("-pnx", help="Play next song", action="store_true")
    playback_parser.add_argument("-rs", help="Resume the currently playing song", action="store_true")
    playback_parser.add_argument("-ps", help="Pause currently playing song", action="store_true")
    playback_parser.add_argument("-vol", help="Adjust the volume of currently playing song", type=int)
    playback_parser.add_argument("-s", help="Search for a track, playlist, show etc. \
                                              Specify as: -search <keyword><space><type>. \
                                              <type> could be any of 'track’, ‘playlist’, ‘show’, and ‘episode’",
                                              type=str, nargs='+')
    playback_parser.add_argument("-dvc", help="Get all your devices", action="store_true")
    playback_parser.add_argument("-q", help="Get user's queue", action="store_true")
    playback_parser.add_argument("-qad", help="Add item to the queue", type=str)
    
    subparsers_actions = [
        action for action in parser._actions if isinstance(action, argparse._SubParsersAction)
    ]

    help_text = "\n" + parser.format_help() 
    for subparsers_action in subparsers_actions:
        # get all subparsers and print help
        for choice, subparser in subparsers_action.choices.items():
            help_text += f"{'_' * 130}\n\n" + subparser.format_help()

    if not os.path.isfile(".env"):
        print("Please create .env file and add your 'client_id' and 'client_secret' to it before proceeding")
        sys.exit()
    args = parser.parse_args()
    spfy_client = SpotifyClient()
    if args.h:
        print(help_text)
    elif args.auth:
        spfy_client.authenticate()
    elif args.cr:
        spfy_client.get_currently_playing_song()
    elif args.ppr:
        spfy_client.play_previous_song()
    elif args.pnx:
        spfy_client.play_next_song()
    elif args.rs:
        spfy_client.resume_currently_playing_song()
    elif args.ps:
        spfy_client.pause_currently_playing_song()
    elif args.vol:
        spfy_client.adjust_volume(args.vol)
    elif args.s:
        spfy_client.search(args.s)
    elif args.dvc:
        spfy_client.get_devices()
    elif args.q:
        spfy_client.get_queue()
    elif args.qad:
        spfy_client.add_to_queue(args.qad)
