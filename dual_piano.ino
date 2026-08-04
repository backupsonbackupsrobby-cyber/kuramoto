#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

RF24 radio(9, 10); // CE, CSN hardware mapping lines
const byte address = "8888P";

void setup() {
  Serial.begin(115200);
  
  if (!radio.begin()) {
    Serial.println(F("[-] Antenna hardware not responding. Check physical lines."));
    while (1);
  }
  
  radio.setSPISpeed(17000000);       // Max 17MHz physical hardware speed
  radio.setPALevel(RF24_PA_MIN);     // Bench test power floor safety
  radio.setDataRate(RF24_250KBPS);   // Optimal sensitivity tracking
  radio.setAutoAck(false);           // Disable handshakes (No waiting)
  
  radio.openWritingPipe(address);
  radio.stopListening();             // Pure autonomous broadcast mode
  
  Serial.println(F("[+] Dual-Piano Kuramoto Transmitter Live on Port 8888 Spectrum."));
}

void loop() {
  static unsigned int noteIndex = 0;
  char dataPayload[32];
  
  snprintf(dataPayload, sizeof(dataPayload), "PIANO_NOTE_%u", noteIndex);
  radio.write(&dataPayload, sizeof(dataPayload));
  Serial.println(dataPayload);
  
  noteIndex = (noteIndex + 1) % 88; 
  delay(10); 
}
