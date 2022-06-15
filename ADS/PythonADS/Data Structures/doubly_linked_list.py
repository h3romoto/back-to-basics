from linked_list import *

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
