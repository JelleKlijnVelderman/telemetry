import socket

# Server configuratie
SERVER_IP = '127.0.0.1'  # Luistert op localhost (voor testen op dezelfde machine)
SERVER_PORT = 12346       # Arbitrair poortnummer
BUFFER_SIZE = 1024        # Grootte van het buffer voor ontvangen gegevens

# Socket aanmaken
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind de socket aan het IP en poort
server_socket.bind((SERVER_IP, SERVER_PORT))

# Luisteren naar inkomende verbindingen (maximaal 1 tegelijk)
server_socket.listen(1)
print(f"Server is aan het luisteren op {SERVER_IP}:{SERVER_PORT}")

# Wachten op een inkomende verbinding
client_socket, client_address = server_socket.accept()
print(f"Verbinding geaccepteerd van {client_address}")

# Gegevens ontvangen van de client
while True:
    data = client_socket.recv(BUFFER_SIZE)
    if not data:
        break
    print(f"Gegevens ontvangen: {data.decode()}")

# Sluit de verbindingen
client_socket.close()
server_socket.close()
