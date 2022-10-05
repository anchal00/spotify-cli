import argparse
import os
import sys

from dotenv import load_dotenv

import auth

if __name__ == "__main__":
    load_dotenv()
    parser = argparse.ArgumentParser(description="Control spotify playback using your command line")
    access_token = os.getenv("access_token")
    refresh_token = os.getenv("refresh_token")
    if not bool(access_token and refresh_token):
        is_successful = auth.authenticate()
        if is_successful == False:
            print("Error while completing authentication process")
            print("Exiting....")
            sys.exit()
