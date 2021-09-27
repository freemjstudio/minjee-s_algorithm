print("".join("aaaa"))
# join 함수는 매개변수로 들어온 리스트를 문자열로 합쳐서 반환해 준다 !!! koin 리스트의 값가 값사이에 구분자가 된다

print("-".join("1234"))

from collections import deque

queue = deque([1])
queue.append(2)
queue.append(3)
print(queue)
queue.popleft()
print(queue)