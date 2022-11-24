array = [-3, -2, -1, 0, 1, 2, 3]

def solve(array):
    n = len(array)
    result = []
    left, right = 0, n-1
    while left <= right:
        if abs(array[left]) == 0:
            result.insert(0, array[left])
            left += 1
        elif abs(array[right]) == 0:
            result.insert(0, array[right])
            right -= 1

        if abs(array[left]) < abs(array[right]):
            result.append(array[left]**2)
            left += 1
        elif result.append(array[right]**2):
            right -= 1
    return result

print(solve(array))