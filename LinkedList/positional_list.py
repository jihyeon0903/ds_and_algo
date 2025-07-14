from doubly_linked import DoublyLinkedBase

class PositionalList(DoublyLinkedBase):
  class Position:
    def __init__(self, container, node):
      self.container = container
      self.node = node

    def element(self):
      return self.node.element

    def __eq__(self, other):
      return type(other) is type(self) and other.node is self.node

    def __ne__(self, other):
      return not (self == other)

    def _validate(self, p):
      if not isinstance(p, self.Position):
        raise TypeError('p must be proper Position type')
      if p.container is not self:
        raise ValueError('p does not belong to this container')
      """
      setting node.next = None is a convention used to mark that a node is no longer part of the list — in other words, it’s been invalidated or deleted.
      """
      if p.node.next is None:
        raise ValueError('p is no longer valid')
      return p.node

    def _make_position(self, node):
      if node is self.header or node is self.trailer:
        return None
      else:
        return self.Position(self, node)

    def first(self):
      return self._make_position(self.header.next)

    def last(self):
      return self._make_position(self.trailer.prev)

    def before(self, p):
      node = self._validate(p)
      return self._make_position(node.prev)

    def after(self, p):
      node = self._validate(p)
      return self._make_position(node.next)

    def iter(self):
      cursor = self.first()
      while cursor is not None:
        yield cursor.element
        cursor = self.after(cursor)

    def _insert_between(self, e, predecessor, successor):
      node = super()._insert_between(e, predecessor, successor)
      return self._make_position(node)

    def add_first(self, e):
      return self._insert_between(e, self.header, self.header.next)

    def add_last(self, e):
      return self._insert_between(e, self.trailer.prev, self.trailer)

    def add_before(self, p, e):
      original = self._validate(p)
      return self._insert_between(e, original.prev, original)

    def add_last(self, p, e):
      original = self._validate(p)
      return self._insert_between(e, original, original.next)

    def delete(self, p):
      original = self._validate(p)
      return self.delete_node(original)

    def replace(self, p, e):
      original = self._validate(p)
      old_value = original.element
      original.element = e
      return old_value

  # sorting
  def insertion_sort(L):
    if len(L) > 1:
      marker = L.first()
      while marker != L.last():
        pivot = L.after(marker)
        val = pivot.element
        if val > marker.element():
          marker = pivot
        else:
          walk = marker
          while walk != L.first() and L.before(walk).element() > val:
            walk = L.before(walk)
          L.delete(pivot)
          L.add_before(walk, val)