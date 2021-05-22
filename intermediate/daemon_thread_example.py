import threading
import time
import random

names = ["John", "Max", "Brian", "Joe", "Chloe", "Wilson", "Bob", "Calvin"]


def greeting():
    while True:
        print(f"Greeting, {random.choice(names)}!")
        time.sleep(3)


def counter():
    for x in range(1, 10):
        print(x)
        time.sleep(1)
    print("Ended")


greeting_thread = threading.Thread(target=greeting, daemon=True)
counter_thread = threading.Thread(target=counter)

greeting_thread.start()
counter_thread.start()
