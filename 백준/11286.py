# 11286 절댓값 힙
import sys

N = int(sys.stdin.readline())
array = []

for _ in range(N):
    num = int(sys.stdin.readline())
    if num != 0:
        array.append(num)
    else:
        result = []
        min_abs = array[0]
        for i in array:
            if abs(i) < min_abs:
                min_abs = abs(i)

        for i in array:
            if abs(i) == min_abs:
                result.append(i)

        print(min(result))
        array.remove(min(result))


