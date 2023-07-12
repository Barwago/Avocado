# Digital Vinyl - RFID Spotify Integration

Welcome to the world of Digital Vinyl, where the retro meets the futuristic! Get ready to groove and rock out to your favorite Spotify playlists with a touch of your RFID cards/tags. Say goodbye to flipping vinyl records and hello to a new way of enjoying music. Let's dive into the details.

## What is Digital Vinyl?

Digital Vinyl is a project that combines the nostalgia of vinyl records with the convenience of digital music streaming. By associating your RFID cards/tags with Spotify playlists, you can instantly play your favorite tunes with just a touch. It's like having a personalized jukebox at your fingertips!

## Requirements

- Arduino Edition:
  - Arduino board with RFID-RC522 module (Uno, Mega, etc.)
  - Arduino IDE
  - MFRC522 library (install via Arduino Library Manager)
  - Jumper wiers (Male to Female)
  - serial library (`pip install serial`)
  - spotipy library (`pip install spotipy`)
  - webbrowser library (`pip install webbrowser`)

- Raspberry Pi Edition:
  - Raspberry Pi board
  - Python 3
  - Jumper wiers (Female to Female)
  - pi-rc522 library (`pip install pi-rc522`)
  - spotipy library (`pip install spotipy`)

## How to Set Up Digital Vinyl

### Arduino Edition

1. Connect the RFID-RC522 module to your Arduino board using the provided wiring diagram. Double-check the connections to ensure they are correct.

        +---------------------+      +----------------------+
        |       Arduino       |      |     RFID-RC522       |
        |                     |      |                      |
        |        3.3V    ------+-----> 3.3V                 |
        |        GND     ------+-----> GND                  |
        |        9       ------+-----> RST                  |
        |        10      ------+-----> SDA (SS)             |
        |        11      ------+-----> MOSI                 |
        |        12      ------+-----> MISO                 |
        |        13      ------+-----> SCK                  |
        +---------------------+      +----------------------+

2. Install the necessary libraries in your Arduino IDE. The required library for this project is the MFRC522 library. You can install it via the Arduino Library Manager.

3. Open the Arduino sketch provided (`Arduino_RFID.ino`) in the Arduino IDE.

4. Connect your Arduino board to your computer via USB.

5. Upload the sketch to your Arduino board using the Arduino IDE. Wait for the upload process to complete.

6. Now, the Arduino board is ready to read the UID of your RFID cards/tags and send it to your computer.

7. Open the python script provided (`DigitalVinyl_Arduino.py`)

8. Modify the code to customize your RFID card to playlist mappings. Look for the `uid_playlist_mapping` dictionary and update it with your desired mappings. Use the UID of each RFID card/tag as the key and the Spotify playlist URI as the value.

9. Run the python script in the same serial port as the arduino code is running in. 

### Raspberry Pi Edition

1. Connect the RFID-RC522 module to your Raspberry Pi and get ready to embark on a sonic adventure.

        +---------------------+      +----------------------+
        |   Raspberry Pi      |      |     RFID-RC522       |
        |                     |      |                      |
        |        3.3V    ------+-----> 3.3V                 |
        |        GND     ------+-----> GND                  |
        |        19       ------+-----> MOSI                 |
        |        21       ------+-----> MISO                 |
        |        23       ------+-----> SCLK                 |
        |        24       ------+-----> SDA (SS)             |
        |        22       ------+-----> RST                  |
        +---------------------+      +----------------------+

2. Install the necessary dependencies: Python 3, pip, and the enchanting libraries (`pi-rc522` and `spotipy`).

3. Open the `DigitalVinyl_Raspberrypi.py` file and prepare to customize the enchanting `uid_playlist_mapping` dictionary. Associate your magical RFID card UIDs with the captivating Spotify playlist URIs that set your soul on fire.

4. Save the file and unleash the power of the Python script by making it executable (`chmod +x DigitalVinyl_Raspberrypi.py.py`).

5. Now, it's time to let the music take over! Run the Python script (`./DigitalVinyl_Raspberrypi.py.py`) and experience the wonders of Digital Vinyl.

## Let the Music Play!

- Arduino Edition: Spin your RFID card/tag on the turntable of possibilities. As the Arduino sketch reads the UID, it checks if it matches any of the card UIDs in the `uid_playlist_mapping` array. When a match is found, it sends the corresponding playlist URI to your computer over the serial port. Let the music take control as you use this URI to orchestrate Spotify playback from your computer.

- Raspberry Pi Edition: Ignite the atmosphere with the flick of a card. As the Python script reads the UID, it checks if it matches any of the card UIDs in the enchanting `uid_playlist_mapping` dictionary. When a match is found, it unlocks the gateway to your desired playlist. Watch as the Spotify playlist URL opens in a web browser, and the music starts playing magically using the Spotipy library.

Get ready to groove with Digital Vinyl and embark on a musical journey like never before!

Note: Keep your Spotify credentials (client ID, client secret) handy and make sure the redirect URI is set up correctly for Spotify authentication.

## License

This project is licensed under the [MIT License](LICENSE). So, get creative, remix, reimagine, and share the joy of Digital Vinyl with the world!

Get your RFID cards/tags ready, pump up the volume, and let the Digital Vinyl experience elevate your music enjoyment to a whole new level!
