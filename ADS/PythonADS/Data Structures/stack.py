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