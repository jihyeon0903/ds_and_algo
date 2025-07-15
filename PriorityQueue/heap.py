# array-based is especially suitable for a complete binary tree
from unsorted import PriorityQueueBase
from LinkedList.positional_list import PositionalList

class HeapPriorityQueue(PriorityQueueBase):
  def __init__(self):
    self._data = PositionalList()

  # Nonpublic behaviors
  def _parent(self, j):
    # parent index
    return (j-1) // 2

  def _left(self, j):
    # left child index
    return 2 * j + 1

  def _right(self, j):
    # right child index
    return 2 * j + 2

  def _has_left(self, j):
    # if left index within the bound
    return self._left(j) < len(self._data)

  def _has_right(self, j):
    # if right index within the bound
    return self._right(j) < len(self._data)

  def _swap(self, i, j):
    self._data[i], self._data[j] = self._data[j], self._data[i]

  def _upheap(self, j):
    parent = self._parent(j)
    # if j's key is smaller than its parent's key
    if j > 0 and self._data[j] < self._data[parent]:
      self._swap(j, parent)
      self._upheap(parent)

  def _downheap(self, j):
    if self._has_left(j):
      left = self._left(j)
      small_child = left
      if self._has_right(j):
        right = self._right(j)
        if self._data[right] < self._data[left]:
          small_child = right
      if self._data[small_child] < self._data[j]:
        self._swap(j, small_child)
        self._downheap(small_child)

  # Public behaviors
  def __len__(self):
    return len(self._data)

  def add(self, key, value):
    self._data.append(self._Item(key, value))
    self._upheap(len(self._data)-1)

  def min(self):
    if self.is_empty():
      raise ValueError('priority queue is emtpy')
    item = self._data[0]
    return (item._key, item._value)

  def remove_min(self):
    if self.is_empty():
      raise ValueError('priority queue is emtpy')
    # swap the root with the last element
    self._swap(0, len(self._data) - 1)
    item = self._data.pop()
    self._downheap(0)
    return (item._key, item._value)