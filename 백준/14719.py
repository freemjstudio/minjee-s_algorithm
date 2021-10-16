h, w = map(int, input().split())
height = list(map(int, input().split()))

maxH = 1
maxL = 0

for i in range(len(height)):
    if maxH < height[i]:
        maxH = height[i]
        maxIndex = i

total = 0
temp = 0

for i in range(maxIndex+1): 
    if height[i] > temp:
        temp = height[i]
    total += temp

temp = 0
for i in range(w-1, maxIndex, -1):
    if height[i] > temp:
        temp = height[i]
    total += temp
print(total - sum(height))

