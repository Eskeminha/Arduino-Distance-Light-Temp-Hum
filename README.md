
<p align="center">
  <img alt="Build" src="https://img.shields.io/badge/build-manual-bluegrey?style=flat-square">
  <img alt="License" src="https://img.shields.io/badge/license-Acadêmico-blue?style=flat-square">
  <img alt="Platform" src="https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-blue?style=flat-square">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python">
  <img alt="Flask" src="https://img.shields.io/badge/Framework-Flask-black?style=flat-square&logo=flask">
  <img alt="Arduino" src="https://img.shields.io/badge/Hardware-Arduino-green?style=flat-square&logo=arduino">
  <img alt="Status" src="https://img.shields.io/badge/status-em%20desenvolvimento-yellow?style=flat-square">
</p>

# 📟 Arduino Distance Light Temp Hum

Projeto completo que integra sensores de **temperatura (DHT11)**, **distância (HC-SR04)** e **luminosidade (HM Photosensor)** com um **servidor web Flask**, exibindo os dados em tempo real com visual moderno, barra de intensidade de luz e indicadores visuais de status.

---

## 🛠️ Requisitos

### 🔧 Arduino
- Placa Arduino Uno ou compatível
- Arduino IDE instalado
- Biblioteca `DHTlib` instalada (`DHTlib-master.zip`)

### 🖥️ Python + Flask
- Python 3.8+
- Biblioteca `pyserial`
- Biblioteca `flask`

Instale com:

```bash
pip install -r requirements.txt
```

---

## ⚙️ Como usar

### 🧩 Etapa 1: Código Arduino

1. Abra o código `.ino` no Arduino IDE
2. Instale a biblioteca `DHTlib`:
   - Vá em **Sketch > Incluir Biblioteca > Adicionar biblioteca .ZIP...**
   - Selecione o arquivo `DHTlib-master.zip`
3. Faça o upload para o Arduino

### 🌐 Etapa 2: Servidor Flask

1. Acesse a pasta `web-server`:

```bash
cd web-server
```

2. Ative seu ambiente virtual (opcional, mas recomendado):

```bash
../venv/Scripts/activate   # Windows
source ../venv/bin/activate  # Linux/macOS
```

3. Execute o servidor:

```bash
python app.py
```

4. Acesse no navegador:
```
http://127.0.0.1:5000
```

A página será atualizada automaticamente a cada segundo, com um **indicador verde/vermelho** para status de leitura (OK/Erro) e uma **barra de intensidade de luz** baseada na leitura invertida (quanto mais claro, maior o valor da barra).

---

## 🔌 Esquema de Conexões

### ✅ DHT11 Sensor (Temperatura e Umidade)
| Pino Sensor | Pino Arduino |
|-------------|--------------|
| S           | D7           |
| +           | 5V           |
| –           | GND          |

### ✅ HC-SR04 Sensor Ultrassônico (Distância)
| Pino Sensor | Pino Arduino |
|-------------|--------------|
| Trig        | D9           |
| Echo        | D10          |
| VCC         | 5V           |
| GND         | GND          |

### ✅ HM Photosensor (Luminosidade)
| Pino Sensor     | Pino Arduino |
|------------------|--------------|
| VCC              | 5V           |
| GND              | GND          |
| Analog Out       | A0           |
| Digital Out (op) | Ignorado     |

---

## 📊 Intensidade de Luz com Barra Visual

A leitura do sensor de luminosidade agora é exibida também com uma **barra de intensidade horizontal**, invertida para refletir de forma intuitiva:

- 💡 **Mais claro → barra cheia**
- 🌑 **Mais escuro → barra vazia**

Isso permite identificar rapidamente mudanças de iluminação no ambiente de forma visual.

---

## 📁 Estrutura do Projeto

```
📦 ARDUINO-DISTANCE-LIGHT-TEMP-HUM
├── projetoluzdisttempumid/
│   └── projetoluzdisttempumid.ino
├── venv/
├── web-server/
│   ├── app.py
│   └── DHTlib-master.zip
├── README.md
├── requirements.txt
└── testecom.py
```

---

## 🚀 Possibilidades de Expansão

- 📈 Adição de gráficos (Chart.js)
- 📤 Envio para banco de dados (InfluxDB, Firebase)
- 🌍 Deploy online via Flask + ngrok ou FastAPI

---

## 🏷️ Tags

`arduino` `flask` `iot` `sensor` `web-dashboard` `real-time` `hc-sr04` `dht11` `photosensor` `python` `serial` `microcontroller` `hardware`

---

## 🧠 Créditos

Desenvolvido por [Seu Nome ou GitHub]  
Com inspiração em projetos didáticos de integração entre hardware e web.
