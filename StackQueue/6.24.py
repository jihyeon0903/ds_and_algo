"""
Implement stack ADT using a single queue as an instance variable, and only constant additional memory within the method bodies.
Running time of push(), pop(), top() -> O(1)
"""

from queue import ArrayQueue

class QueueStack:
  def __init__(self):
    self.S = ArrayQueue()

  def __str__(self):
    return str(self.S)

  def push(self, e):
    # enqueue() adds item at the back
    # push() adds item at the back
    self.S.enqueue(e)

  def pop(self):
    # dequeue() removes the first item
    # pop() removes the last item
    if self.S.is_empty():
      raise Exception("Stack is empty")
    front, last = self.S.data[0], self.S.data[-1]
    self.S.data[0], self.S.data[-1] = last, front
    self.S.dequeue()
    self.S.data[0] = front
    return last

stack = QueueStack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)
stack.push(7)
stack.push(8)
stack.push(9)
stack.push(10)
print(stack)

print(stack.pop())
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)