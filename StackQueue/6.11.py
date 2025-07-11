"""
Adapter that implements queue ADT while using a collections.deque instance for storage
"""
from collections import deque

class DequeToQueueAdapter:
  def __init__(self):
    self.Q = deque()

  def is_empty(self):
    return len(self.Q) == 0

  def enqueue(self, e):
    self.Q.append(e)

  def dequeue(self):
    if self.is_empty():
      return "Queue is empty"
    return self.Q.popleft()

  def first(self):
    if self.is_empty():
      return "Queue is emtpy"
    return self.Q[0]