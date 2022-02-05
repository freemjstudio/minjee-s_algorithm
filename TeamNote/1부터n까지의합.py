def consecutive_sum(start, end):
    if start == end:
        return start
    mid = (start + end) //2
    return consecutive_sum(start, mid) + consecutive_sum(mid+1, end)

print(consecutive_sum(1, 5))