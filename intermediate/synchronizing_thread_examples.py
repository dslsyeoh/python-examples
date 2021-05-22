import threading
import time

lock = threading.Lock()


def counter():
    lock.acquire()
    for x in range(1, 11):
        print(x)
        time.sleep(1)
    lock.release()


def rewind():
    lock.acquire()
    for x in range(9, 0, -1):
        print(x)
        time.sleep(1)
    lock.release()


def run_thread(thread_number):
    thread_name = f"Thread {thread_number}"
    print(f"{thread_name} is trying to acquire")
    bounded_semaphore.acquire()
    print(f"{thread_name} is acquired")
    time.sleep(10)
    print(f"{thread_name} is released")
    bounded_semaphore.release()


def run_threads():
    for x in range(1, 11):
        thread = threading.Thread(target=run_thread, args=(x,))
        thread.start()
        time.sleep(1)


counter_thread = threading.Thread(target=counter)
rewind_thread = threading.Thread(target=rewind)
bounded_semaphore = threading.BoundedSemaphore(5)

print("Start")
time.sleep(1)
counter_thread.start()
rewind_thread.start()
rewind_thread.join()
print("End")

run_threads()


