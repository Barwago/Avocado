import qrcode
import cv2
import webbrowser
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pyzbar import pyzbar
import time
import threading
import pygame

# Generate QR code for a Spotify song
def generate_qr_code(song_url):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(song_url)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")
    qr_img.save("static/song_qr_code.png")

# Spotify credentials
client_id = "42cf26a1f56c46348068db2173db1102"
client_secret = "aa86f90810c94bc79139bc67449d6cad"
redirect_uri = "http://localhost:8888/callback"

# Open the Spotify song URL in a web browser
def open_spotify_url(url):
    try:
        webbrowser.open(url)
    except Exception as e:
        print("Error opening URL:", str(e))

# Start playing the song using Spotipy
def start_playing_song(device_id, track_id):
    try:
        scope = "user-modify-playback-state"
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                       client_secret=client_secret,
                                                       redirect_uri=redirect_uri,
                                                       scope=scope))
        sp.transfer_playback(device_id=device_id, force_play=True)
        sp.start_playback(device_id=device_id, uris=[f"spotify:track:{track_id}"])
    except Exception as e:
        print("Error starting playback:", str(e))


# Extract the track ID from the Spotify song URL
def extract_track_id(url):
    try:
        track_id = url.split("/")[-1].split("?")[0]
        return track_id
    except Exception as e:
        print("Error extracting track ID:", str(e))

# Display and scan the QR code
def scan_qr_code():
    cap = cv2.VideoCapture(0)
    last_scanned_time = 0  # Time of the last scanning process
    delay_duration = 2  # Delay duration in seconds

    def play_sound():
        pygame.mixer.init()
        pygame.mixer.music.load("static/beep.wav")
        pygame.mixer.music.play()
        time.sleep(0.5)
        pygame.mixer.music.stop()

    while True:
        _, frame = cap.read()
        
        cv2.imshow("Scan QR Code", frame)
        # Set a timeout for keyboard interrupt
        try:
            cv2.waitKey(1)
        except KeyboardInterrupt:
            break

        if (time.time() - last_scanned_time) >= delay_duration:  # Delayed start of scanning
            # Convert the frame to grayscale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            # Detect QR codes in the grayscale frame
            qrcodes = pyzbar.decode(gray)
            
            for qr in qrcodes:
                decoded_info = qr.data.decode('utf-8')
                # Check if the decoded information is a valid URL
                if decoded_info.startswith("http"):
                    song_url = decoded_info
                    print("Scanned QR Code URL:", song_url)
                    # Generate QR code for the song
                    generate_qr_code(song_url)
                    # Get the active device ID
                    scope = "user-read-playback-state"
                    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                                   client_secret=client_secret,
                                                                   redirect_uri=redirect_uri,
                                                                   scope=scope))
                    devices = sp.devices()
                    for device in devices['devices']:
                        if device['is_active']:
                            device_id = device['id']
                            track_id = extract_track_id(song_url)
                            start_playing_song(device_id, track_id)
                    play_sound()
                    # Open the Spotify song URL and start playing the song
                    open_spotify_url(song_url)
                    
                    last_scanned_time = time.time()  # Update the last scanned time

    cap.release()
    cv2.destroyAllWindows()

# Play sound when QR code is detected and processed
pygame.init()
pygame.mixer.music.load("static/beep.wav")

# Start QR code scanning in a separate thread
qr_scanning_thread = threading.Thread(target=scan_qr_code)
qr_scanning_thread.start()
