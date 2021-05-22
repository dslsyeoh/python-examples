from collections import deque
import queue

que = ["a", "b", "c"]

print(f"\ninitial queue: {que}")
while que:
    print(f"popped {que.pop(0)} from queue.")
print(f"queue: {que}")

que = ["a", "b", "c"]

print(f"\ninitial queue: {que}")

while que:
    print(f"popped {que.pop()} from queue.")
print(f"queue: {que}")

que = deque(["a", "b", "c"])

print(f"\ninitial queue: {que}")
while que:
    print(f"popped {que.popleft()} from queue.")
print(f"queue: { [] if not que else que }")

que = queue.Queue(maxsize=3)
print(f"\nQueue size: {que.qsize()}")

que.put(1)
que.put(2)
que.put(3)

print(f"Full: {que.full()}")
while not que.empty():
    print(f"popped {que.get()} from queue.")
print(f"Empty: {que.empty()}")

que.put(1)
print(f"Empty: {que.empty()}")
print(f"Full: {que.full()}")

print("\nInitialize queue")
que = queue.LifoQueue()

for x in range(1, 11):
    que.put(x)

while not que.empty():
    print(f"popped {que.get()} from queue.")

print("\nInitialize queue")
que = queue.PriorityQueue()
que.put((1, "Hello World"))
que.put((11, 100))
que.put((5, 12.50))
que.put((100, "Goodbye"))

while not que.empty():
    result = que.get()
    print(f'popped "{result[1]}" from queue with priority: {result[0]}')
