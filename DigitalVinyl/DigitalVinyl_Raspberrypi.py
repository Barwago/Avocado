import webbrowser
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep
from mfrc522 import SimpleMFRC522

'''
sudo apt update
sudo apt install python3 python3-pip

sudo pip3 install pi-rc522
sudo pip3 install spotipy


Make python file executable:
chmod +x DigitalVinyl.py
./DigitalVinyl.py
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
    '565151983455': 'spotify:playlist:5SSifdafznIV2WlWRhtUlL',
    '702624753505': 'spotify:playlist:6I8dvOiPMKSoX2NDOs5vsO',
    '1047304529914': 'spotify:playlist:2UfCYMheuXqkA5NBUkWEwg',
    '154253453078': 'spotify:playlist:37i9dQZF1DXcBWIGoYBM5M',
    '1061894010287': 'spotify:playlist:1OyVxImCy5jDspmOlwTWa6',
    '85367973703': 'spotify:playlist:5clXhwPHeAv6NnCUpgpA6i'
}  # Modify with desired UID-to-playlist mappings

# Create an instance of the RFID class

reader = SimpleMFRC522()
try:
    while True:
        id = reader.read()[0]
        card_uid = str(id)
        print("The ID for this card is:", card_uid)

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
    print("Keyboard interrupt detected. Exiting...")
finally:
    GPIO.cleanup()
