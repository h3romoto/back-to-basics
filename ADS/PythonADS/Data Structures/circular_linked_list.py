from linked_list import *

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