
<p align="center">
  <img alt="Build" src="https://img.shields.io/badge/build-manual-bluegrey?style=flat-square">
  <img alt="License" src="https://img.shields.io/badge/license-Academic-blue?style=flat-square">
  <img alt="Platform" src="https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-blue?style=flat-square">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python">
  <img alt="Flask" src="https://img.shields.io/badge/Framework-Flask-black?style=flat-square&logo=flask">
  <img alt="Arduino" src="https://img.shields.io/badge/Hardware-Arduino-green?style=flat-square&logo=arduino">
  <img alt="Status" src="https://img.shields.io/badge/status-in%20development-yellow?style=flat-square">
</p>

# 📟 Arduino Distance Light Temp Hum

This project combines **temperature (DHT11)**, **distance (HC-SR04)**, and **light intensity (HM Photosensor)** sensors into a single Arduino setup, displaying real-time readings on a modern Flask-based web dashboard with a light intensity bar and status indicators.

---

## 🛠️ Requirements

### 🔧 Arduino
- Arduino Uno or compatible board
- Arduino IDE installed
- `DHTlib` library (`DHTlib-master.zip`)

### 🖥️ Python + Flask
- Python 3.8+
- `pyserial` library
- `flask` library

Install dependencies with:

```bash
pip install -r requirements.txt
```

---

## ⚙️ How to Use

### 🧩 Step 1: Arduino Code

1. Open the `.ino` code file in the Arduino IDE
2. Install the `DHTlib` library:
   - Go to **Sketch > Include Library > Add .ZIP Library...**
   - Select `DHTlib-master.zip`
3. Upload the code to your Arduino board

### 🌐 Step 2: Flask Web Server

1. Navigate to the `web-server` folder:

```bash
cd web-server
```

2. Activate your virtual environment (optional, but recommended):

```bash
../venv/Scripts/activate   # Windows
source ../venv/bin/activate  # Linux/macOS
```

3. Start the server:

```bash
python app.py
```

4. Open your browser and go to:
```
http://127.0.0.1:5000
```

The dashboard updates every second, showing a green/red LED indicator for serial read status, and a light bar that reflects the environment's brightness (inverted: the brighter the room, the fuller the bar).

> 🔸 The HTML layout is now separated into an external template file.

---

## 🔌 Wiring Diagram

### ✅ DHT11 Sensor (Temperature and Humidity)
| Sensor Pin | Arduino Pin |
|------------|--------------|
| S          | D7           |
| +          | 5V           |
| –          | GND          |

### ✅ HC-SR04 Ultrasonic Sensor (Distance)
| Sensor Pin | Arduino Pin |
|------------|--------------|
| Trig       | D9           |
| Echo       | D10          |
| VCC        | 5V           |
| GND        | GND          |

### ✅ HM Photosensor (Light Intensity)
| Sensor Pin      | Arduino Pin |
|------------------|-------------|
| VCC              | 5V          |
| GND              | GND         |
| Analog Out       | A0          |
| Digital Out (opt)| Not used    |

---

## 📊 Light Intensity Bar

The light sensor reading is visually represented as a horizontal progress bar, inverted for clarity:

- 💡 **Brighter → full bar**
- 🌑 **Darker → empty bar**

This makes ambient light changes immediately visible and intuitive.

---

## 📁 Project Structure

```
📦 ARDUINO-DISTANCE-LIGHT-TEMP-HUM
├── projetoluzdisttempumid/
│   └── projetoluzdisttempumid.ino
├── venv/
├── web-server/
│   ├── app.py
│   ├── DHTlib-master.zip
│   └── template.html
├── README.md
├── requirements.txt
└── testecom.py
```

---

## 🚀 Possible Expansions

- 📈 Add dynamic graphs with Chart.js
- 📤 Export data to databases (InfluxDB, Firebase)
- 🌍 Online deployment with Flask + ngrok or FastAPI

---

## 🏷️ Tags

`arduino`, `flask`, `iot`, `sensor`, `web-dashboard`, `real-time`, `hc-sr04`, `dht11`, `photosensor`, `python`, `serial`, `microcontroller`, `hardware`

---

## 🧠 Credits

Developed by [Your Name or GitHub]  
Inspired by educational projects that blend hardware and web integration.
