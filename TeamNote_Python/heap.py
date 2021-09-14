class heap(object):
    def __init__(self, items):
        self.queue = [None] + items

        for i in range(len(self.queue)//2, 0, -1):
            self.max_heapify(i)

    def parent(self, index):
        return index//2

    def left_child(self, index):
        return index*2

    def right_child(self, index):
        return index*2 +1

    def swap(self, i, parent_index):
        self.queue[i], self.queue[parent_index] = self.queue[parent_index], self.queue[i]

    def insert(self, n):
        self.queue.append(n)
        for i in range(len(self.queue)//2, 0, -1):
            self.max_heapify(i)

    def delete(self):
        last_index = len(self.queue) - 1
        if last_index == 0:
            return -1 # queue is empty

        self.swap(1, last_index)
        max_value = self.queue.pop()
        self.max_heapify(1) # root 에서부터 재정렬한다
        return max_value

    def max_heapify(self, i):
        last_index = len(self.queue) - 1
        left_index = self.left_child(i)
        right_index = self.right_child(i)
        temp_max_index = i # 임시적으로 자기 자신을 max라고 생각한다 즉 임시 root 노드

        if left_index <= last_index and self.queue[temp_max_index] < self.queue[left_index]:
            temp_max_index = left_index
        if right_index <= last_index and self.queue[temp_max_index] < self.queue[right_index]:
            temp_max_index = right_index
        # 만약 자기 자신이 가장 큰게 아니면 heapify
        if temp_max_index != i:
            self.swap(i, temp_max_index) # temp_max_index 가 루트 노드로 변경
            self.max_heapify(temp_max_index)

    def print_heap(self):
        print(self.queue)

max_heap = heap([1,2])
max_heap.insert(1)
max_heap.insert(3)
max_heap.insert(5)
max_heap.print_heap()
max_heap.delete()
max_heap.print_heap()