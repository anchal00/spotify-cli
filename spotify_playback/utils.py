def print_artists_info(artists):
    for serial_number, artist in enumerate(artists):
        print(f"Artist {serial_number + 1} -- " + artist["name"])

def print_track_info(track):
    print("_________________________________")
    print("Track name - {}".format(track.get("name")))
    print("Album - {}".format(track.get("album")["name"]))
    print("URI - {}".format(track.get("uri")))
    print("ID - {}".format(track.get("id")))
    print_artists_info(track.get("artists"))
    print(f"_________________________________",end="\n\n")

def print_album_info(album):
    print("_________________________________")
    print("Album name - {}".format(album.get("name")))
    print("Type - {}".format(album.get("album_type")))
    print("Tracks - {}".format(album.get("total_tracks")))
    print("URI - {}".format(album.get("uri")))
    print("ID - {}".format(album.get("id")))
    print_artists_info(album.get("artists"))
    print(f"_________________________________",end="\n\n")

def print_playlist_info(playlist):
    print("_________________________________")
    print("Playlist name - {}".format(playlist.get("name")))
    print("Owner - {}".format(playlist.get("owner").get("display_name")))
    print("Tracks - {}".format(playlist.get("tracks").get("total")))
    print("URI - {}".format(playlist.get("uri")))
    print("ID - {}".format(playlist.get("id")))
    print("_________________________________",end="\n\n")