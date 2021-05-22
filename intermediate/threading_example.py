import threading
import time


def greeting():
    print("Hello World")


def countdown():
    for x in range(10, -1, -1):
        print(x)
        time.sleep(1)


countdown_thread = threading.Thread(target=countdown)
countdown_thread.start()
countdown_thread.join()

greeting()
