import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def start():
    client.connect(("localhost", 5555))
    print(client.recv(1024).decode("utf-8"))
    client.send("Hello World".encode("utf-8"))
    client.close()


start()
