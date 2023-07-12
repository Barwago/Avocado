import webbrowser
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep
from pi_rc522 import RFID

'''
sudo apt update
sudo apt install python3 python3-pip

sudo pip3 install pi-rc522
sudo pip3 install spotipy


Make python file executable:
chmod +x rfid_spotify.py
./rfid_spotify.py
'''

# Spotify credentials
client_id = "42cf26a1f56c46348068db2173db1102"
client_secret = "aa86f90810c94bc79139bc67449d6cad"
redirect_uri = "http://localhost:8888/callback"

# Open the Spotify playlist URL in a web browser
def open_spotify_url(url):
    try:
        webbrowser.open(url)
    except Exception as e:
        print('Error opening URL:', str(e))

# Start playing the playlist using Spotipy
def start_playing_playlist(playlist_uri):
    try:
        scope = 'user-modify-playback-state'
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                       client_secret=client_secret,
                                                       redirect_uri=redirect_uri,
                                                       scope=scope))
        sp.start_playback(context_uri=playlist_uri)
    except Exception as e:
        print('Error starting playback:', str(e))

# Define the card UID to playlist URI mapping
uid_playlist_mapping = {
    'f73dd0b5': 'spotify:playlist:5SSifdafznIV2WlWRhtUlL',
    'ed8de530': 'spotify:playlist:6I8dvOiPMKSoX2NDOs5vsO',
    '24fc3eac': 'spotify:playlist:2UfCYMheuXqkA5NBUkWEwg',
    '20056a1f': 'spotify:playlist:37i9dQZF1DXcBWIGoYBM5M',
    '96be04e8': 'spotify:playlist:1OyVxImCy5jDspmOlwTWa6',
    '049390baf06280': 'spotify:playlist:5clXhwPHeAv6NnCUpgpA6i'
}  # Modify with desired UID-to-playlist mappings

# Create an instance of the RFID class
rfid = RFID()

try:
    while True:
        # Wait for a card to be detected
        rfid.wait_for_tag()

        # Request the UID of the detected card
        (error, tag_type) = rfid.request()

        if not error:
            # Get the UID of the card
            (error, uid) = rfid.anticoll()

            if not error:
                # Convert the UID to a string
                card_uid = ''.join([str(i) for i in uid])

                print('Card UID:', card_uid)

                # Check if the card UID exists in the mapping
                if card_uid in uid_playlist_mapping:
                    playlist_uri = uid_playlist_mapping[card_uid]
                    print('Playing playlist:', playlist_uri)
                    # Open the Spotify playlist URL and start playing the playlist
                    open_spotify_url(playlist_uri)
                    start_playing_playlist(playlist_uri)

        # Delay before detecting the next card
        sleep(0.1)

except KeyboardInterrupt:
    # Clean up the RFID module
    rfid.cleanup()
