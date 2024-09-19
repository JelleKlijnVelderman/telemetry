from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import socket

# Server configuratie
SERVER_IP = '127.0.0.1'
SERVER_PORT = 12345
BUFFER_SIZE = 1024

# Flask app en SocketIO setup
app = Flask(__name__)
socketio = SocketIO(app)

# Route voor de homepage
@app.route('/')
def index():
    return render_template('index.html')

# Functie om telemetriegegevens door te sturen naar de front-end
def send_telemetry_data():
    # Maak de socket aan voor het ontvangen van data van de racewagen
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_IP, SERVER_PORT))
    server_socket.listen(1)
    print(f"Server luistert op {SERVER_IP}:{SERVER_PORT}")

    # Wachten op verbinding
    client_socket, client_address = server_socket.accept()
    print(f"Verbonden met {client_address}")

    # Ontvangen en doorsturen van gegevens
    while True:
        data = client_socket.recv(BUFFER_SIZE)
        if not data:
            break
        sensor_data = data.decode()

        try:
            # Verzend de ontvangen data naar de front-end via SocketIO
            socketio.emit('telemetry_update', {'data': sensor_data})
        except Exception as e:
            print(f"Fout bij het verwerken van data: {e}")

    client_socket.close()
    server_socket.close()

# Start de server en begin met het ontvangen van data
if __name__ == '__main__':
    socketio.start_background_task(send_telemetry_data)
    socketio.run(app, debug=True)
