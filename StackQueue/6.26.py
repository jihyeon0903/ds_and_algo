"""
1. Implement double-ended queue ADT using two stacks.
2. Find out the running tims of the methods.
"""

from stack import ArrayStack

class StackToDeque:
  def __init__(self):
    self.s1 = ArrayStack()
    self.s2 = ArrayStack()

  def __str__(self):
    return str(self.s1) + " / " + str(self.s2)

  def add_last(self, e):
    # O(1)
    self.s1.push(e)

  def add_first(self, e):
    # O(n)
    if len(self.s1) == 0:
      self.s1.push(e)
    else:
      self.s2.push(e)
      while len(self.s1) != 0:
        item = self.s1.pop()
        self.s2.push(item)
      while len(self.s2) != 0:
        item = self.s2.pop()
        self.s1.push(item)

  def delete_last(self):
    # O(1)
    if len(self.s1) == 0:
      return "Queue is empty"
    return self.s1.pop()

  def delete_first(self):
    # O(n)
    if len(self.s1) == 0 and len(self.s2) == 0:
      return "Queue is empty"
    while len(self.s1) != 0:
      item = self.s1.pop()
      self.s2.push(item)
    return self.s2.pop()


stack_to_deque = StackToDeque()
stack_to_deque.add_last(1)
print(stack_to_deque)
stack_to_deque.add_first(0)
print(stack_to_deque)
stack_to_deque.add_first(90)
print(stack_to_deque)
stack_to_deque.delete_first()
print(stack_to_deque)
stack_to_deque.delete_last()
print(stack_to_deque)