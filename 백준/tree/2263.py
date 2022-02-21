# 2263 트리의 순회
import sys
sys.setrecursionlimit(10**6)

n = int(input())
position = [0]*(n+1)

inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

for i in range(n):
    position[inorder[i]] = i
# preorder : root -> left child -> right child

def preorder(in_start, in_end, post_start, post_end):
    # 재귀 종료 조건 - start와 end 가 만나는 지점에서 종료
    if (in_start > in_end) or (post_start > post_end):
        return
    root = postorder[post_end]
    print(root, end=" ") # root

    left = position[root] - in_start
    right = in_end - position[root]
    # left child
    preorder(in_start, in_start+left-1, post_start, post_start+left-1)
    # right child
    preorder(in_end-right+1, in_end, post_end - right, post_end-1)

preorder(0, n-1, 0, n-1)
