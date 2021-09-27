from collections import deque

queue = deque()

queue.append(1) # [  1 ]
queue.append(2)
queue.append(3)
queue.append(4)

print(queue)
queue.popleft()
print(queue)
queue.reverse()
print(queue)

def factorial_iteration(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

def factorial_recursive(n):
    if n <= 1:
        return 1
    return factorial_recursive(n-1)*n

print(factorial_iteration(10))
print(factorial_recursive(10))
