from collections import deque

queue = deque() # empty queue declaration

queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft() # 맨 처음 큐에 들어온 1이 pop 된다 !

print(queue)

queue.popleft() # 2
print(queue)

queue.popleft() # 3
print(queue)

queue.popleft()