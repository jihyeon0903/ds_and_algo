from map_base import MapBase

class SortedTableMap(MapBase):
  # ----- nonpublic behavior -----
  def _find_index(self, k, low, high):
    """
    Return index of the leftmost item with key greater than or equal to k
    Return high + 1 if no such item qualifies
    """
    if high < low:    # k is greater than all keys
      return high + 1    # correct insertion position
    else:
      mid = (low + high) // 2
      if k == self._table[mid]._key:    # found exact match
        return mid
      elif k < self._table[mid]._key:
        return self._find_index(k, low, mid - 1)    # search the left half
      else:
        return self._find_index(k, mid + 1, high)    # search the right half

  # ----- public behavior -----
  def __init__(self):
    self._table = []

  def __len__(self):
    return len(self._table)

  def __getitem__(self, k):
    j = self._find_index(k, 0, len(self._table) - 1)
    if j == len(self.table) or self._table[j]._key != k:
      raise KeyError('Key Error: ' + repr(k))
    return self._table[j]._value

  def __setitem__(self, k, v):
    j = self._find_index(k, 0, len(self._table) - 1)
    if j < len(self._table) and self._table[j]._key == k:    # found the match
      self._table[j]._value = v    # replace the value
    else:
      self._table.insert(j, self._Item(k,v))    # add new item

  def __delitem__(self, k):
    j = self._find_index(k, 0, len(self._table) - 1)
    if j == len(self._table) or self._table[j]._key != k:
      raise KeyError('Key Error: ' + repr(k))
    self._table.pop(j)

  def __iter__(self):
    for item in self._table:
      yield item._key

  def __reversed__(self):
    for item in reversed(self._table):
      yield item._key

  def find_min(self):
    if len(self._table) > 0:
      return (self._table[0]._key, self._table[0]._value)
    else:
      return None

  def find_max(self):
    if len(self._table) > 0:
      return (self._table[-1]._key, self._table[-1]._value)
    else:
      return None

  # Find the first entry with key ≥ k
  def find_ge(self, k):
    """
    For _table = [(1, A), (3, B), (4, C), (7, D)]:
      •	find_ge(4) → (4, C)
      •	find_ge(5) → (7, D)
      •	find_ge(8) → None
    """
    j = self._find_index(k, 0, len(self._table) - 1)
    if j < len(self._table):
      return (self._table[j]._key, self._table[j]._value)
    else:
      return None

  # Find the first entry with key > k
  def find_gt(self, k):
    j = self._find_index(k, 0, len(self._table) - 1)
    if j < len(self._table) and self._table[j]._key == k:
      j += 1
    if j < len(self._table):
      return (self._table[j]._key, self._table[j]._value)
    else:
      return None

  # Find the last entry with key < k
  def find_lt(self, k):
    """
    For _table = [(1, A), (3, B), (4, C), (7, D)]:
      •	find_ge(4) → (4, C)
      •	find_ge(5) → (7, D)
      •	find_ge(8) → None
    """
    j = self._find_index(k, 0, len(self._table) - 1)
    if j > 0:
      return (self._table[j-1]._key, self._table[j-1]._value)
    else:
      return None

  def find_range(self, start, stop):    # O(s+logn) time
    if start is None:
      j = 0
    else:
      j = self._find_index(start, 0, len(self._table) - 1)
    while j < len(self._table) and (stop is None or self._table[j]._key < stop):
      yield (self._table[j]._key, self._table[j]._value)
      j += 1