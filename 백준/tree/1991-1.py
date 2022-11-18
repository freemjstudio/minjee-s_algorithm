# 트리 순회
# 중위 순회
n = int(input())
tree = {}
for i in range(n):
    a, b, c = input().split()
    tree[a] = [b, c]

def preorder(root):
    if root != '.':
        left, right = tree[root]
        print(root, end='')
        preorder(left)
        preorder(right)

def inorder(root):
    if root != '.':
        left, right = tree[root]
        inorder(left)
        print(root, end='')
        inorder(right)

def postorder(root):
    if root != '.':
        left, right = tree[root]
        postorder(left)
        postorder(right)
        print(root, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')