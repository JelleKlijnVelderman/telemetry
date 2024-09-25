import socket
import time
import json
import random  # Voeg deze import toe

SERVER_IP = '127.0.0.1'
SERVER_PORT = 12345

# Maak een verbinding met de server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, SERVER_PORT))

while True:
    # Genereer willekeurige telemetriegegevens
    snelheid = random.randint(0, 199)  # Willekeurige snelheid tussen 0 en 199
    temperatuur = random.randint(0, 70)  # Willekeurige temperatuur tussen 0 en 70

    # Maak een dictionary van de telemetriegegevens
    telemetrie_data = {
        'snelheid': snelheid,
        'temperatuur': temperatuur
    }

    # Zet de dictionary om naar een JSON-string
    telemetrie_json = json.dumps(telemetrie_data)

    # Stuur de JSON-string naar de server
    client_socket.sendall(telemetrie_json.encode())

    # Wacht 1 seconde voor de volgende meting
    time.sleep(1)

client_socket.close()
