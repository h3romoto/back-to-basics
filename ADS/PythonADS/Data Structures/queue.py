# QUEUES
# FIFO - First In First Out
# enqueue(), dequeue()
# Uses the double-ended queue aka Deque provided by Python
# Deque can add and remove items from both ends of the queue

class Queue():
  def __init__(self) -> None:
    self.queue = list()

  def enqueue(self, item):
    self.queue.append(item)

  def dequeue(self):
    if (len(self.queue) > 0):
      self.queue.pop[len(self.queue)-1]
    else:
      return None
