import socket
import time

HOST = "localhost"
PORT = 5555
FORMAT = "UTF-8"
ADDRESS = (HOST, PORT)
DISCONNECT_MESSAGE = "!DISCONNECT"


def connect():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDRESS)
    return client


def send(client, message):
    msg = message.encode(FORMAT)
    client.send(msg)


def start():
    answer = input("Would you like to connect (y/n): ")
    if answer.lower() != "y":
        return

    client = connect()

    while True:
        message = input("Message (q for quit): ")
        if message.lower() == "q":
            break
        send(client, message)
    send(client, DISCONNECT_MESSAGE)
    time.sleep(1)
    print("Disconnected")


start()



