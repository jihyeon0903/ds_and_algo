"""
Implement the queue ADT using two stacks,
such that all queue operations execute in O(1)* time.
"""

from stack import ArrayStack

class StackToQueue:
  def __init__(self):
    self.s1 = ArrayStack()
    self.s2 = ArrayStack()

  def __str__(self):
    return str(self.s2)

  def enqueue(self, e):
    self.s1.push(e)

  def dequeue(self):
    if len(self.s1) == 0 and len(self.s2) == 0:
      return "Queue is empty"
    while len(self.s1) != 0:
      item = self.s1.pop()
      self.s2.push(item)
    return self.s2.pop()

stack_to_queue = StackToQueue()
stack_to_queue.enqueue(1)
stack_to_queue.enqueue(2)
stack_to_queue.enqueue(3)
print(stack_to_queue)

print(stack_to_queue.dequeue())
print(stack_to_queue.dequeue())
print(stack_to_queue.dequeue())


# formal proof
# n enqueue --> 1 dequeue (1 dequeue while loop for every n enqueue operation)
# Therefore, amortized bound of O(1) for dequeue operation
