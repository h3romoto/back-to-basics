from collections import deque

# HEAPS
class Heap():
    def __init__(self) -> None:
        self.heap = deque()
    def append(self, item):
        self.heap.append(item)
    def pop(self):
        if len(self.heap) > 0:
            self.heap.popleft()
        else:
            return None
    def __str__(self) -> str:
        return str(self.heap)

# my_heap = Heap()
# my_heap.append(4)
# my_heap.append(5)
# my_heap.append(8)
# print(my_heap)
# my_heap.pop()
# print(my_heap)