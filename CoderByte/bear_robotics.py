stack = [1,2,3,4,5]

def insert(val):
    stack.append(val)

def remove(val):
    stack.remove(val)

# 중복 허용하지 않고

def remove_first():
    stack.pop(0)

def check_insert(val):
    set_stack = set(stack)
    if val not in set_stack:
        stack.append(val)
    else:
        print("duplicated!")

insert(10)
print(stack)
remove(10)
print(stack)
check_insert(5)
check_insert(6)
print(stack)
remove_first()
print(stack)