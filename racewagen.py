import socket
import time
import random

# Client configuratie
SERVER_IP = '127.0.0.1'  # IP van de server
SERVER_PORT = 12345       # Moet hetzelfde zijn als op de server
SENSOR_DATA_INTERVAL = 2  # Tijd in seconden tussen verzenden van sensor data

# Socket aanmaken
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Verbinding maken met de server
client_socket.connect((SERVER_IP, SERVER_PORT))
print(f"Verbonden met de server op {SERVER_IP}:{SERVER_PORT}")

# Simuleren van sensorgegevens
try:
    while True:
        # Simuleren van wat sensorgegevens (bv. snelheid en temperatuur)
        snelheid = random.randint(50, 200)  # Random snelheid tussen 50 en 200 km/u
        temperatuur = random.uniform(20.0, 100.0)  # Random temperatuur tussen 20°C en 100°C

        # Maak een string met de sensorgegevens
        sensor_data = f"Snelheid: {snelheid} km/u, Temperatuur: {temperatuur:.2f} °C"
        print(f"Versturen: {sensor_data}")

        # Verstuur de gegevens naar de server
        client_socket.send(sensor_data.encode())

        # Wacht een paar seconden voor het versturen van de volgende gegevens
        time.sleep(SENSOR_DATA_INTERVAL)

except KeyboardInterrupt:
    # Verbreek de verbinding bij Ctrl+C
    print("\nVerbinding verbreken...")
    client_socket.close()
