
#include <SPI.h>
#include <SD.h>
#include <RTClib.h>

#define SD_PIN 10
#define SAMPLE_INTERVAL_US 20000  // 50 Hz = 20 ms

RTC_DS1307 rtc;
File dataFile;
char fileName[13];

unsigned long lastSampleTime = 0;
unsigned long sampleCount = 0;

const char header[] PROGMEM = "Timestamp(us),AnalogValue";

void setup() {
  Serial.begin(9600);

  if (!rtc.begin()) {
    Serial.println(F("No se encuentra el módulo RTC"));
    while (1);
  }

  if (!rtc.isrunning()) {
    rtc.adjust(DateTime(F(__DATE__), F(__TIME__)));
  }

  if (!SD.begin(SD_PIN)) {
    Serial.println(F("Error al inicializar la tarjeta SD"));
    while (1);
  }

  DateTime now = rtc.now();
  snprintf(fileName, sizeof(fileName), "%02d%02d%02d.txt",
           now.hour(), now.minute(), now.second());

  dataFile = SD.open(fileName, FILE_WRITE);
  if (!dataFile) {
    Serial.println(F("Error al abrir el archivo"));
    while (1);
  }

  dataFile.println((__FlashStringHelper*)header);
  dataFile.flush();

  lastSampleTime = micros();
}

void loop() {
  unsigned long now = micros();

  if (now - lastSampleTime >= SAMPLE_INTERVAL_US) {
    lastSampleTime += SAMPLE_INTERVAL_US;

    int value = analogRead(A0);

    char line[32];
    snprintf(line, sizeof(line), "%lu,%d\n", sampleCount * SAMPLE_INTERVAL_US, value);
    dataFile.print(line);

    sampleCount++;

    if (sampleCount % 10 == 0) {
      dataFile.flush();
    }
  }
}
