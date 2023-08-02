import webbrowser
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep

CLIENT_ID="6ee36b187eeb4a85aa4a3d43cfcbeedb"
CLIENT_SECRET="493d80960800417b9efbeb6f958edca2"

# Spotify Authentication
# Spotify Authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                client_secret=CLIENT_SECRET,
                                                redirect_uri="http://localhost:8080",
                                                scope="user-read-playback-state,user-modify-playback-state"))

# Play the spotify track at URI with ID 45vW6Apg3QwawKzBi03rgD (you can swap this for a diff song ID below)
sp.start_playback(uris=['spotify:track:45vW6Apg3QwawKzBi03rgD'])