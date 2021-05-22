import threading

event = threading.Event()


def my_event():
    print("Waiting for event to trigger...")
    event.wait()
    print("Performing action...")


event_thread = threading.Thread(target=my_event)
event_thread.start()

result = input("Enter y to trigger event: ")
if result == "y":
    event.set()
