# 2263 트리의 순회

n = int(input())
for _ in range(n):
    inorder = list(map(int, input().split()))
    postorder = list(map(int, input().split()))

# preorder : root -> left child -> right child

def preorder(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return
    root = postorder[post_end]
    print(root, end=" ") # root
    root_index = inorder.index(root)
    # left child
    preorder(in_start, root_index-1, in_start, root_index)
    # right child
    preorder(root_index+1, in_end, root_index+1, post_end)

preorder(0, n-1, 0, n-1)
