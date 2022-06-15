# MAX HEAPS (implementation can be transformed into a mean heap)
# A complete binary tree where each child node <= parent node
# Implemented using lists 
# Similar to stacks and heaps
# Always pop max in O(1) time
# Insert in O(logn) time
# Remove max in O(logn)
# Operations are pop(), peek(), push()
class MaxHeap:
    def __init__(self, items=[]) -> None:
        super().__init__()
        # dont use the first index element
        self.heap = [0]
        for item in items:
            self.heap.append(item)
            self.__floatUp(len(self.heap) - 1)

    def push(self, data):
        self.heap.append(data)
        self.__floatUp(len(self.heap) - 1)

    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return False
    
    def pop(self):
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap) - 1)
            max = self.heap.pop()
            self.__bubbleDown(1)
        elif len(self.heap) == 2:
            # only two elements on the heap
            max = self.heap.pop()
        else:
            max = False
        return max

    def __swap(self,  i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __floatUp(self, index):
        parent = index//2
        if index < 1:
            return
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__floatUp(parent)
    
    def __bubbleDown(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self.__swap(index, largest)
            self.__bubbleDown(largest)

    def __str__(self) -> str:
        return str(self.heap)


# m = MaxHeap([95, 3, 21])
# m.push(10)
# print(m)
# print(m.pop())
# print(m.peek())
