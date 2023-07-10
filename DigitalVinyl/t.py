import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Spotify credentials
client_id = "42cf26a1f56c46348068db2173db1102"
client_secret = "aa86f90810c94bc79139bc67449d6cad"
redirect_uri = "http://localhost:8888/callback"

# Get the active device ID
def get_active_device_id():
    scope = "user-read-playback-state"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                   client_secret=client_secret,
                                                   redirect_uri=redirect_uri,
                                                   scope=scope))
    devices = sp.devices()
    for device in devices['devices']:
        if device['is_active']:
            return device['id']
    return None

# Call the function to get the active device ID
device_id = get_active_device_id()
if device_id:
    print("Active Device ID:", device_id)
else:
    print("No active device found.")