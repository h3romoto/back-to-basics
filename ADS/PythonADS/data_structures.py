## lists, tuples, strings

# x = "cmptr"
# y = (1, 8, 4, 5)
# print(len(x))
# # min and max are determined lexicographically
# print(min(x))
# print(sum(y))
# # sorted does not change original, returns a list
# z = sorted(y)

# a = ['Tanaka', 'Trymore', 'Ngoni', 'Nkosi', 'Kuda', 'Rati']
# # sort based on nth letter
# print(sorted(a, key=lambda k:k[1]))
# print(z)
# #count items in a sequence
# print(a[0].count('a'))    #3
# #index of first appearance of item in seq
# print(a[0].index('a'))    #1
# #unpacking, variables should match items in seq
# anim = ['huku', 'bhiza', 'mombe']
# b, c, d = anim
# print(c)

# for index, item in enumerate(x):
#     print(index, item)


# # LISTS

# # sortable
# # grow and shrink size as needed
# # multiple data types

# li = list()    #new list
# # list comprehensions
# li = [i for i in range(4)]
# print(li)

# del(li[2])
# li.append('x')


# # STACKS
# # LIFO - Last In First Out
# # Can only operate at the top of the stack
# # push(), pop(), peek()
# # e.g the command stack, web page history
# # implemented using List with a Wrapper Class 
class Stack():
    def __init__(self) -> None:
        self.stack = list()
    def push(self, item):
        self.stack.append(item)
    def pop(self,item):
        if len(self.stack) > 0:
            self.stack.pop(item)
        else:
            return None
    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack)-1]
        else:
            return None
    def __str__(self) -> str:
        return str(self.stack)

# my_stack = Stack()
# my_stack.push(3)
# my_stack.push(34)
# my_stack.push(10)
# print(my_stack.peek())


# QUEUES
# FIFO - First In First Out
# enqueue(), dequeue()
# Uses the double-ended queue aka Deque provided by Python
# Deque can add and remove items from both ends of the queue

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

#  Dan 
# 50722244832

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


# LINKED LISTS
# Attributes: root, size
# Operations: find(data), add(data), remove(data), print_list()
from hashlib import new


class Node:
    def __init__(self, d, n=None, p=None) -> None:
        self.data = d
        self.next = n
        self.prev = p

    def __str__(self) -> str:
        return ('(' + str(self.data) + ')')


class LinkedList:
    def __init__(self,  r = None) -> None:
        self.root = r
        self.size = 0
    
    def add(self, d):
        # uses the Node class
        new_node = Node(d, self.root)
        self.root = new_node
        self.size += 1

    def find(self, d):
        this_node = self.root
        while this_node != None:
            if this_node.data == d:
                return this_node
            else:
                # replaced this_node = this_node.next_node with ... 
                this_node = this_node.next
        return None

    def remove(self, d):
        this_node = self.root
        prev_node = None

        while this_node is not None:
            if this_node.data == d:
                if prev_node is not None:
                    # data is in non-root
                    prev_node.next = this_node.next
                else:
                    # data is in root node
                    self.root = this_node.next
                self.size -= 1
                return True
            else:
                prev_node = this_node
                this_node = this_node.next
        return False

    def print_list(self):
        this_node = self.root
        while this_node is not None:
            print(this_node, end='->')
            this_node = this_node.next
        print(None)

# myList = LinkedList()
# myList.add(5)
# myList.add(8)
# myList.add(12)
# myList.print_list()


class CircularLinkedList:
    def __init__(self,  r = None) -> None:
        self.root = r
        self.size = 0
    
    def add(self, d):
        if self.size == 0:
            self.root = Node(d)
            self.root.next = self.root
        else:
            new_node = Node(d, self.root.next)
            self.root.next = new_node
        self.size += 1

    def find(self, d):
        this_node = self.root

        while True:
            if this_node.data == d:
                return d
            elif this_node.next == self.root:
                return False
            this_node = this_node.next

    def remove(self, d):
        this_node = self.root
        prev_node = None

        while True:
            if this_node.data == d:
                if prev_node is not None:
                    # data is in non-root
                    prev_node.next = this_node.next
                else:
                    while this_node.next != self.root:
                        this_node = this_node.next
                    this_node.next = self.root.next
                    self.root = this_node.next
                self.size -= 1
                return True
            elif this_node.next == self.root:
                return False
            prev_node = this_node
            this_node = this_node.next

    def print_list(self):
        if self.root is None:
            return 
        this_node = self.root
        print(this_node, end='->')
        while this_node.next != self.root:
            this_node = this_node.next
            print(this_node, end='->')
        print(None)

# cll = CircularLinkedList()
# for i in [5, 7, 3, 8, 9]:
#     cll.add(i)

# print("size="+str(cll.size))
# print(cll.find(8))
# print(cll.find(12))
# my_node = cll.root
# print(my_node, end='->')
# for i in range(8):
#     my_node = my_node.next
#     print(my_node, end='->')
# print()


class DoublyLinkedList:
    def __init__(self,  r = None) -> None:
        self.root = r
        self.last = r
        self.size = 0
    
    def add(self, d):
        if self.size == 0:
            self.root = Node(d)
            self.last = self.root
        else:
            new_node = Node(d, self.root)
            self.root.prev = new_node
            self.root = new_node
        self.size += 1

    def find(self, d):
        this_node = self.root
        while this_node is not None:
            if this_node.data == d:
                return d
            elif this_node.next == None:
                return False
            else:
                this_node = this_node.next
        return None

    def remove(self, d):
        this_node = self.root
        while this_node is not None:
            if this_node.data == d:
                if this_node.prev is not None:
                    if this_node.next is not None:
                        this_node.prev.next = this_node.next
                        this_node.next.prev = this_node.prev
                    else:   # delete the last node
                        this_node.prev.next = None
                        self.last = this_node.prev
                else:
                    # data is in root node
                    self.root = this_node.next
                    this_node.next.prev = self.root
                self.size -= 1
                return True
            else:
                this_node = this_node.next
        return False    # data not found 

    def print_list(self):
        this_node = self.root
        while this_node is not None:
            print(this_node, end='->')
            this_node = this_node.next
        print(None)

# dll = DoublyLinkedList()
# for i in [5, 9, 3, 8, 9]:
#     dll.add(i)

# print("size="+str(dll.size))
# dll.print_list()
# dll.remove(8)
# print("size="+str(dll.size))
# print(dll.remove(15))
# print(dll.find(15))
# dll.add(21)
# dll.add(22)
# dll.remove(5)
# dll.print_list()
# print(dll.last.prev)




# TREES
# BINARY TREE
# each node is greater than every node in it's left subtree
# each node is less than every node in it's right subtree
# Operations: insert(), find(), delete(), get_size(), traversals
# insert(), find(), delete() are O(log n)
# Inserts start at the root (at the top of the tree) and then "bubble down"
class Tree:
    def __init__(self, data, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right

    def insert(self, data):
        if self.data == data:
            return False
        elif self.data > data:
            if self.left is not None:
                return self.left.insert(data)
            else:
                self.left = Tree(data)
                return True
        else:
            if self.right is not None:
                return self.right.insert(data)
            else:
                self.right = Tree(data)
                return True
    
    def find(self, data):
        if self.data == data:
            return data
        elif self.data > data:
            if self.left is None:
                return False
            else:
                return self.left.find(data)
        elif self.data < data:
            if self.right is None:
                return False
            else:
                self.right.find(data)

    def delete(self, data):
        pass
    
    def get_size(self):
        if self.left is not None and self.right is not None:
            return 1 + self.left.get_size() + self.right.get_size()
        elif self.left:
            return 1 + self.left.get_size()
        elif self.right:
            return 1 + self.right.get_size()
        else:
            return 1
    
    def preorder(self):
        if self is not None:
            print(self.data, end=' ')
            if self.left is not None:
                self.left.preorder()
            if self.right is not None:
                self.right.preorder()
    
    def inorder(self):
        if self is not None:
            if self.left is not None:
                self.left.inorder()
            print(self.data, end=' ')
            if self.right is not None:
                self.right.inorder()
            
# tree = Tree(7)
# tree.insert(9)
# for i in [15, 10, 2, 12, 3, 1, 13, 6, 11, 4, 14, 9]:
#     tree.insert(i)

# for i in range(16):
#     print(tree.find(i), end=' ')
# print('\n', tree.get_size())

# tree.preorder()
# print()
# tree.inorder()
# print()



# GRAPH
# 2 implementations: Adjaceny List, Adjacency Matrix
# Adjacency lists are fit for sparse graph
# Adjacency matrices are fir for dense graphs and for weighted graph

class Vertex:
    def __init__(self, n) -> None:
        self.name = n
        self.neighbors = set()

    def add_neighbor(self, v):
        self.neighbors.add(v)

# Adjacency List implementation
class ALGraph:
    vertices = {}
    
    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            self.vertices[u].add_neighbor(v)
            self.vertices[v].add_neighbor(u)
            return True
        else:
            False

    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key, sorted(list(self.vertices[key].neighbors)))

# g = ALGraph()
# a = Vertex('A')
# g.add_vertex(a)
# g.add_vertex('B')
# for i in range (ord('A'), ord('K')):
#     g.add_vertex(Vertex(chr(i)))

# edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ']
# for edge in edges:
#     g.add_edge(edge[0], edge[1])

# g.print_graph()

 

 # Adjacency matrix implementation
class AMGraph:
    vertices = {}
    edges = []
    edge_indices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            # for loop appends a column of zeros to the edges matrix
            for row in self.edges:
                row.append(0)
            
            # append a row of zeros to the bottom of the edges matrix
            self.edges.append([0] * (len(self.edges)+1))
            self.edge_indices[vertex.name] = len(self.edge_indices)
            return True
        else:
            return False

    def add_edge(self, u, v, weight=1):
        if u in self.vertices and v in self.vertices:
            self.edges[self.edge_indices[u]][self.edge_indices[v]] = weight 
            self.edges[self.edge_indices[v]][self.edge_indices[u]] = weight
            return True
        else:
            return False

    def print_graph(self):
        for v, i in sorted(self.edge_indices.items()):
            print(v + ' ', end=' ')
            for j in range(len(self.edges)):
                print(self.edges[i][j], end=' ')
            print(' ')

g = AMGraph()
a = Vertex('A')
g.add_vertex(a)
g.add_vertex('B')
for i in range (ord('A'), ord('K')):
    g.add_vertex(Vertex(chr(i)))

edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ']
for edge in edges:
    g.add_edge(edge[0], edge[1])

g.print_graph()