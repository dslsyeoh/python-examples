import socket
import threading

HOST = "localhost"
PORT = 5555
FORMAT = "UTF-8"
ADDRESS = (HOST, PORT)
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)

clients = set()
client_lock = threading.Lock()


def handle_client(connection, address):
    print(f'[NEW CONNECTION] "{address}" CONNECTED')

    try:
        connected = True
        while connected:
            message = connection.recv(1024).decode(FORMAT)
            if not message:
                break
            if message == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{address}]: {message}")

            with client_lock:
                for client in clients:
                    client.sendall(f"[{address}]: {message}".encode(FORMAT))
    finally:
        with client_lock:
            clients.remove(connection)
        connection.close()


def start():
    print("[SERVER STARTED]")
    server.listen()

    while True:
        connection, address = server.accept()
        with client_lock:
            clients.add(connection)
        thread = threading.Thread(target=handle_client, args=(connection, address))
        thread.start()


start()
