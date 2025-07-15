from unsorted import PriorityQueueBase
from ..LinkedList import positional_list

class SortedPriorityQueue(PriorityQueueBase):
  # add / min / remove_min
  def __init__(self):
    self._data = positional_list.PositionalList()

  def __len__(self):
    return len(self._data)

  def __str__(self):
    return str(self._data)

  def add(self, key, value):
    new = self._Item(key, value)
    walk = self._data.last()
    while walk is not None and new < walk.element():
      walk = self._data.before(walk)
    if walk is None:
      self._data.add_first(new)
    else:
      self.data.add_after(walk, new)

  def min(self):
    if self.is_empty():
      raise ValueError('priority queue is empty')
    p = self._data.first()
    item = p.element()
    return (item._key, item._value)

  def remove_min(self):
    if self.is_empty():
      raise ValueError('priority queue is empty')
    item = self._data.delete(self._data.first())
    return (item._key, item._value)


sorted_queue = SortedPriorityQueue()
sorted_queue.add(1, 'L')
sorted_queue.add(2, 'J')
print(sorted_queue)
print(sorted_queue.min())
print(sorted_queue.remove_min())
print(sorted_queue.min())