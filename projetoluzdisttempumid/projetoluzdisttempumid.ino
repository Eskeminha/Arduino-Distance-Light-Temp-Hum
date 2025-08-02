#include <dht.h>           // Include the DHT library
dht DHT;

#define DHT11_PIN 7        // DHT11 connected to digital pin 7
#define trigPin 9          // HC-SR04 Trigger pin
#define echoPin 10         // HC-SR04 Echo pin
#define photoPin A0        // HM Photosensor analog output connected to A0

void setup() {
  Serial.begin(9600);

  // Setup pins for HC-SR04
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  // No need to define pinMode for photoPin (analog input)
}

void loop() {
  // ---- Read Temperature & Humidity ----
  DHT.read11(DHT11_PIN);
  float temp = DHT.temperature;
  float hum = DHT.humidity;

  // ---- Read Distance from HC-SR04 ----
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  float duration = pulseIn(echoPin, HIGH);
  float distance = (duration * 0.0343) / 2;

  // ---- Read Light Level from Photosensor ----
  int lightLevel = analogRead(photoPin);

  // ---- Print All Data in One Line ----
  Serial.print("Temp: ");
  Serial.print(temp, 1);         // 1 decimal place
  Serial.print(" C\t");

  Serial.print("Hum: ");
  Serial.print(hum, 1);
  Serial.print(" %\t");

  Serial.print("Dist: ");
  Serial.print(distance, 1);
  Serial.print(" cm\t");

  Serial.print("Light: ");
  Serial.println(lightLevel);    // ends line

  delay(100); // Fast refresh rate for responsiveness
}
