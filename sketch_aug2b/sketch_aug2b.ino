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
  int chk = DHT.read11(DHT11_PIN);
  Serial.print("Temperature (C): ");
  Serial.println(DHT.temperature);
  Serial.print("Humidity (%): ");
  Serial.println(DHT.humidity);

  // ---- Read Distance from HC-SR04 ----
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  float duration = pulseIn(echoPin, HIGH);
  float distance = (duration * 0.0343) / 2;
  Serial.print("Distance (cm): ");
  Serial.println(distance);

  // ---- Read Light Level from Photosensor ----
  int lightLevel = analogRead(photoPin);
  Serial.print("Light Level (0-1023): ");
  Serial.println(lightLevel);

  // ---- Delay between readings ----
  delay(4000); // 1 second
}
