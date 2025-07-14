class LinkedStack:
  class Node:
    __slot__ = 'element', 'next'
    def __init__(self, element, next):
      self.element = element
      self.next = next

  def __init__(self):
    self.head = None
    self.size = 0

  def __len__(self):
    return self.size

  def is_empty(self):
    return self.size == 0

  def push(self, e):
    self.head = self.Node(e, self.head)
    self.size += 1

  def top(self):
    if self.is_empty:
      return "stack is empty"
    return self.head.element

  def pop(self):
    if self.is_empty:
      return "stack is empty"
    answer = self.head.element
    self.head = self.head.next
    self.size -= 1
    return answer