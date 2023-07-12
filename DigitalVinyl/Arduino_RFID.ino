#include <SPI.h>
#include <MFRC522.h>

#define RST_PIN 9
#define SS_PIN 10

MFRC522 mfrc522(SS_PIN, RST_PIN);

void setup() {
  Serial.begin(9600);
  while (!Serial) {
    // Wait for serial connection
  }
  
  SPI.begin();
  mfrc522.PCD_Init();
  mfrc522.PCD_DumpVersionToSerial();
  Serial.println("Scan PICC to see UID...");

  delay(2000); // Delay to allow time to open the serial monitor
}

void loop() {
  if (!mfrc522.PICC_IsNewCardPresent()) {
    return;
  }

  if (!mfrc522.PICC_ReadCardSerial()) {
    return;
  }

  // Send the card UID to the computer via serial communication
  String cardUID = "";
  for (byte i = 0; i < mfrc522.uid.size; i++) {
    cardUID += String(mfrc522.uid.uidByte[i] < 0x10 ? "0" : "");
    cardUID += String(mfrc522.uid.uidByte[i], HEX);
  }
  Serial.println("Card UID: " + cardUID);

  // Send the card UID to the computer
  Serial.println(cardUID);

  // Halt the card to save power
  mfrc522.PICC_HaltA();
  mfrc522.PCD_StopCrypto1();

  delay(2000); // Delay before scanning for the next card
}
