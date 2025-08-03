from flask import Flask, render_template_string, jsonify
import serial
import time
import os

app = Flask(__name__)

last_valid_data = "Please wait until first data comes through..."
last_status = False 
last_light_percent = 0

# Load HTML template from file
TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), 'template.html')
with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
    HTML_TEMPLATE = f.read()

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/data')
def get_data():
    global last_valid_data, last_status, last_light_percent
    try:
        # with serial.Serial(port='COM3', baudrate=9600, timeout=1) as arduino:                         # WINDOWS
        with serial.Serial(port='/dev/cu.usbserial-1410', baudrate=9600, timeout=1) as arduino:         # MAC
            time.sleep(0.5)
            line = ''
            attempts = 0
            while line.strip() == '' and attempts < 5:
                line = arduino.readline().decode('utf-8', errors='ignore').strip()
                attempts += 1

            if line:
                last_valid_data = line
                last_status = True

                # Start the string extraction.
                if "Light:" in line:
                    try:
                        parts = line.split("Light:")
                        value = int(parts[-1].strip().split()[0])
                        inverted = 1023 - value
                        last_light_percent = int((inverted / 1023) * 100)
                    except:
                        last_light_percent = 0
                else:
                    last_light_percent = 0
            else:
                raise Exception("No data received from Arduino.")
    except Exception as e:
        print(f"[SERIAL ERROR] {e}")
        last_status = False

    return jsonify({
        'data': last_valid_data,
        'status': last_status,
        'light_percent': last_light_percent
    })

if __name__ == '__main__':
    app.run(debug=False)