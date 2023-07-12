# Digital Vinyl - RFID Spotify Integration

Welcome to the world of Digital Vinyl, where the retro meets the futuristic! Get ready to groove and rock out to your favorite Spotify playlists with a touch of your RFID cards/tags. Say goodbye to flipping vinyl records and hello to a new way of enjoying music. Let's dive into the details and get the party started!

## What is Digital Vinyl?

Digital Vinyl is a project that combines the nostalgia of vinyl records with the convenience of digital music streaming. By associating your RFID cards/tags with Spotify playlists, you can instantly play your favorite tunes with just a touch. It's like having a personalized jukebox at your fingertips!

## Requirements

- Arduino Edition:
  - Arduino board with RFID-RC522 module
  - Arduino IDE
  - MFRC522 library (install via Arduino Library Manager)

- Raspberry Pi Edition:
  - Raspberry Pi board
  - Python 3
  - pi-rc522 library (`pip install pi-rc522`)
  - spotipy library (`pip install spotipy`)

## How to Set Up Digital Vinyl

### Arduino Edition

1. Connect your Arduino board with the RFID-RC522 module and unleash your inner DJ.

2. Install the MFRC522 library in your Arduino IDE and let the music flow.

3. Open the provided Arduino sketch (`rfid_spotify.ino`) in the Arduino IDE. Feel free to add your personal touch!

4. It's time to create magic! Customize the `uid_playlist_mapping` array in the sketch to associate your RFID card UIDs with the Spotify playlist URIs that make you move and groove.

5. Upload the sketch to your Arduino board and witness the transformation of your RFID cards into musical gateways.

### Raspberry Pi Edition

1. Connect the RFID-RC522 module to your Raspberry Pi and get ready to embark on a sonic adventure.

2. Install the necessary dependencies: Python 3, pip, and the enchanting libraries (`pi-rc522` and `spotipy`).

3. Open the `rfid_spotify.py` file and prepare to customize the enchanting `uid_playlist_mapping` dictionary. Associate your magical RFID card UIDs with the captivating Spotify playlist URIs that set your soul on fire.

4. Save the file and unleash the power of the Python script by making it executable (`chmod +x rfid_spotify.py`).

5. Now, it's time to let the music take over! Run the Python script (`./rfid_spotify.py`) and experience the wonders of Digital Vinyl.

## Let the Music Play!

- Arduino Edition: Spin your RFID card/tag on the turntable of possibilities. As the Arduino sketch reads the UID, it checks if it matches any of the card UIDs in the `uid_playlist_mapping` array. When a match is found, it sends the corresponding playlist URI to your computer over the serial port. Let the music take control as you use this URI to orchestrate Spotify playback from your computer.

- Raspberry Pi Edition: Ignite the atmosphere with the flick of a card. As the Python script reads the UID, it checks if it matches any of the card UIDs in the enchanting `uid_playlist_mapping` dictionary. When a match is found, it unlocks the gateway to your desired playlist. Watch as the Spotify playlist URL opens in a web browser, and the music starts playing magically using the Spotipy library.

Get ready to groove with Digital Vinyl and embark on a musical journey like never before!

Note: Keep your Spotify credentials (client ID, client secret) handy and make sure the redirect URI is set up correctly for Spotify authentication.

## License

This project is licensed under the [MIT License](LICENSE). So, get creative, remix, reimagine, and share the joy of Digital Vinyl with the world!

Get your RFID cards/tags ready, pump up the volume, and let the Digital Vinyl experience elevate your music enjoyment to a whole new level!
