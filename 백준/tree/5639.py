# 5639 이진 검색 트리
import sys
sys.setrecursionlimit(10**6)
tree = []


def postorder(start, end):
    if start > end:
        return
    root = tree[start]
    idx = end+1

    for i in range(start+1, end+1):
        if root < tree[i]:
            idx = i # left sub tree 와 right subtree의 경계가 되는 index
            break
    postorder(start+1, idx-1)
    postorder(idx, end)
    print(root)

while True:
    try:
        tree.append(int(input()))
    except: # EOF 입력되면 에러가 일어나는것을 이용
        break

postorder(0, len(tree)-1)