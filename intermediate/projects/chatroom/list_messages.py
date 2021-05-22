import socket

HOST = "localhost"
PORT = 5555
FORMAT = "UTF-8"
ADDRESS = (HOST, PORT)


def connect():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDRESS)
    return client


def start():
    client = connect()
    while True:
        message = client.recv(1024).decode(FORMAT)
        print(message)


start()
