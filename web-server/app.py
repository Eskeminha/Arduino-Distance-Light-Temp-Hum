from flask import Flask, render_template_string, jsonify
import serial
import time

app = Flask(__name__)

last_valid_data = "Aguardando primeira leitura..."
last_status = False  # False = erro, True = sucesso

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Arduino Sensor Dashboard</title>
    <link rel="icon" href="https://cdn-icons-png.flaticon.com/512/3103/3103472.png" type="image/png">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: #f0f2f5;
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            background: #ffffff;
            padding: 40px;
            border-radius: 12px;
            box-shadow: 0 8px 16px rgba(0,0,0,0.1);
            width: 90%;
            max-width: 600px;
            text-align: center;
        }
        h1 {
            color: #333333;
            font-size: 2rem;
            margin-bottom: 10px;
        }
        .sensor-data {
            background: #f9f9f9;
            border: 1px solid #ddd;
            padding: 20px;
            border-radius: 8px;
            font-size: 1.3rem;
            color: #222;
            white-space: pre-line;
        }
        footer {
            margin-top: 20px;
            font-size: 0.8rem;
            color: #888;
        }
        .led {
            display: inline-block;
            width: 15px;
            height: 15px;
            border-radius: 50%;
            margin-left: 10px;
            border: 1px solid #555;
            background-color: grey; /* initial */
        }
        .status-label {
            font-size: 0.9rem;
            color: #555;
            margin-top: 8px;
        }
    </style>
    <script>
        async function fetchData() {
            try {
                const res = await fetch('/data');
                const json = await res.json();

                document.querySelector('.sensor-data').innerText = json.data;

                const led = document.querySelector('.led');
                led.style.backgroundColor = json.status ? 'green' : 'red';

                const statusText = document.querySelector('.status-label');
                statusText.innerText = json.status ? "Status: Leitura OK" : "Status: Erro na leitura (mostrando último valor)";
            } catch (err) {
                console.error("Erro na leitura do servidor:", err);
            }
        }

        setInterval(fetchData, 1000);
        window.onload = fetchData;
    </script>
</head>
<body>
    <div class="container">
        <h1>📟 Arduino Sensor Dashboard <span class="led"></span></h1>
        <div class="sensor-data">Carregando dados...</div>
        <div class="status-label">Status: aguardando...</div>
        <footer>Atualizado automaticamente a cada segundo.</footer>
    </div>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/data')
def get_data():
    global last_valid_data, last_status
    try:
        with serial.Serial(port='COM3', baudrate=9600, timeout=1) as arduino:
            time.sleep(0.5)
            line = ''
            attempts = 0
            while line.strip() == '' and attempts < 5:
                line = arduino.readline().decode('utf-8', errors='ignore').strip()
                attempts += 1

            if line:
                last_valid_data = line
                last_status = True
            else:
                raise Exception("Linha vazia")
    except Exception as e:
        print(f"[ERRO SERIAL] {e}")
        last_status = False

    return jsonify({'data': last_valid_data, 'status': last_status})

if __name__ == '__main__':
    app.run(debug=False)
