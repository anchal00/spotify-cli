generic_error_message = "Couldn't complete the request. Something went wrong"

def map_http_status_to_reason(http_status):
    http_status_to_reason_mapping = {
        401: "Bad or expired token. Please re-authenticate yourself",
        403: "Bad request",
        409: "Request Limit Exceeded. Cannot handle any further requests"
    }
    return (
        http_status_to_reason_mapping[http_status] if http_status in http_status_to_reason_mapping else generic_error_message
    )

def print_artists_info(artists):
    for serial_number, artist in enumerate(artists):
        print(f"Artist {serial_number + 1} -- " + artist["name"])

def print_track_info(track):
    print(f"_________________________________")
    print("Track name - {}".format(track.get("name")))
    print("Album - {}".format(track.get("album")["name"]))
    print("URI - {}".format(track.get("uri")))
    print_artists_info(track.get("artists"))
    print(f"_________________________________",end="\n\n")

def print_album_info(album):
    print(f"_________________________________")
    print("Album name - {}".format(album.get("name")))
    print("Type - {}".format(album.get("album_type")))
    print("Tracks - {}".format(album.get("total_tracks")))
    print("URI - {}".format(album.get("uri")))
    print_artists_info(album.get("artists"))
    print(f"_________________________________",end="\n\n")
