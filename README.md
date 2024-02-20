### SPOTIFY-CLI 🎸

Control spotify playback using your command line

Tested on Python Version: 3.8.15

Run `python spotify_cli.py -h` for usage details

#### Commands

```
positional arguments:
  {playback}  Sub commands for controlling playback

optional arguments:
  -auth       Authorize with spotify APIs
  -h          Help
__________________________________________________________________________________________________________________________________

usage: spotify_cli.py playback [-h] [-cr] [-ppr] [-pnx] [-rs] [-ps] [-vol VOL] [-s S [S ...]] [-dvc] [-q] [-qad QAD]

Playback controls

optional arguments:
  -h, --help    show this help message and exit
  -cr           Get currently playing song
  -ppr          Play previous song
  -pnx          Play next song
  -rs           Resume the currently playing song
  -ps           Pause currently playing song
  -vol VOL      Adjust the volume of currently playing song
  -s S [S ...]  Search for a track, playlist, show etc. Specify as: -search <keyword><space><type>. <type> could be any of 'track’, ‘playlist’, ‘show’, and ‘episode’
  -dvc          Get all your devices
  -q            Get user's queue
  -qad QAD      Add item to the queue
```
