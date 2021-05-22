import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 5555))


def start():
    server.listen()
    print("[SERVER STARTED]")

    try:
        while True:
            connection, address = server.accept()
            print(f"[{address}] CONNECTED!")
            connection.send("You are connected.".encode("utf-8"))
            print(f'[{address}]: {connection.recv(1024).decode("utf-8")}')
    finally:
        server.close()


start()

