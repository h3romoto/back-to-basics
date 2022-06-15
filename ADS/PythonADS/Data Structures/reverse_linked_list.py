import time

class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None
  
  # Function to print the list
  def printList(self):
    node = self
    output = '' 
    while node != None:
      output += str(node.val)
      output += " "
      node = node.next
    print(output)

  # Iterative Solution
  def reverseIteratively(self, head):
    previous = None         # `previous` initially points to None
    current = head     # `current` points at the first element
    following = current.next    # `following` points at the second element

    # go till the last element of the list
    while current:
      current.next = previous # reverse the link
      previous = current      # move `previous` one step ahead
      current = following         # move `current` one step ahead
      if following:               # if this was not the last element
          following = following.next    # move `following` one step ahead
    head = previous

  # Recursive Solution      
  def reverseRecursively(self, head):
    pass
    # Implement this.

# Test Program
# Initialize the test list:
testHead = ListNode('e')

node1 = ListNode('d')
testHead.next = node1

node2 = ListNode('c')
node1.next = node2

node3 = ListNode('b')
node2.next = node3

testTail = ListNode('a')
node3.next = testTail
print("Initial list: ")
testHead.printList()
# 4 3 2 1 0
testHead.reverseIteratively(testHead)
#testHead.reverseRecursively(testHead)
print("List after reversal: ")
testTail.printList()
# 0 1 2 3 4


