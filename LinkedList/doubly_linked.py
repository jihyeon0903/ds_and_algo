class DoublyLinkedBase:
  class Node:
    __slot__ = 'element', 'next'
    def __init__(self, element, next):
      self.element = element
      self.next = next

  # header and trailer --> dummy nodes
  def insert_between(self, e, predecessor, successor):
    newest = self.Node(e, predecessor, successor)
    predecessor.next = newest
    successor.prev = newest
    self.size += 1
    return newest

  def delete_node(self, node):
    predecessor = node.prev
    successor = node.next
    predecessor.next = node.next
    successor.prev = predecessor
    self.size -= 1
    element = node.element
    node.prev = node.next = node.element = None
    return element


class LinkedDeque(DoublyLinkedBase):
  def first(self):
    if self.is_empty():
      return 'deque is emtpy'
    return self.header.next.element

  def last(self):
    if self.is_empty():
      return 'deque is emtpy'
    return self.trailer.prev.element

  def insert_first(self, e):
    self.insert_between(e, self.header, self.header.next)

  def insert_last(self, e):
    self.insert_between(e, self.trailer.prev, self.trailer)

  def delete_first(self):
    if self.is_empty():
      return 'deque is emtpy'
    return self.delete_node(self.header.next)

  def delete_last(self):
    if self.is_empty():
      return 'deque is emtpy'
    return self.delete_node(self.trailer.prev)