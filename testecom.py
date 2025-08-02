import serial

try:
    arduino = serial.Serial('COM3', 9600, timeout=1)
    print("Conectado com sucesso!")
    arduino.close()
except Exception as e:
    print("Erro:", e)