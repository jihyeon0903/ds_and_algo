from map_base import MapBase
import random

class HashMapBase(MapBase):
  def __init__(self, cap=11, p=109345121):
    self._table = cap * [None]
    self._n = 0
    self._prime = p
    self._scale = 1 + random.randrange(p-1)
    self._shift = random.randrange(p)

  def _hash_function(self, k):
    return (hash(k) * self._scale + self._shift) % self._prime % len(self._table)

  def __len__(self):
    return self._n

  def __getitem__(self, k):
    j = self._hash_function(k)
    return self._bucket_getitem(j, k)

  def __setitem__(self, k, v):
    j = self._hash_function(k)
    self._bucket_setitem(j, k, v)
    if self._n > len(self._table) // 2:
      self._resize(2 * len(self._table) - 1)

  def __delitem__(self, k):
    j = self._hash_function(k)
    self._bucket_delitem(j, k)
    self._n -= 1

  def _resize(self, c):
    # use iteration to record existing items
    old = list(self.items())
    self._table = c * [None]
    self._n = 0
    for (k, v) in old:
      self[k] = v


# Separate Chaining
from unsorted_table_map import UnsortedTableMap

class ChainHashMap(HashMapBase):
  def _bucket_getitem(self, j, k):
    bucket = self._table[j]
    if bucket is None:
      raise KeyError('Key Error: ' + repr(k))
    return bucket[k]

  def _bucket_setitem(self, j, k, v):
    if self._table[j] is None:
      # new bucket to the table
      self._table[j] = UnsortedTableMap()
    oldsize = len(self._table[j])
    self._table[j][k] = v
    if len(self._table[j]) > oldsize:
      # increase overall map size as new item is added
      self._n += 1

  def _bucket_delitem(self, j, k):
    bucket = self._table[j]
    if bucket is None:
      raise KeyError('Key Error: ' + repr(k))
    del bucket[k]

  def __iter__(self):
    for bucket in self._table:
      # only non-empty buckets
      if bucket is not None:
        for key in bucket:
          yield key


# Linear Probing
class ProbeHashMap(HashMapBase):
  _AVAIL = object()

  def _is_available(self, j):
    # return true if j is available
    return self._table[j] is None or self._table[j] is ProbeHashMap._AVAIL

  def _find_slot(self, j, k):
    """
    Return (success, index) tuple
    -> if match is found, success is true and index denotes its location
    -> if no match found, success is false and index denotes the first available slot
    """

    firstAvail = None
    while True:
      if self._is_available(j):
        if firstAvail is None:
          firstAvail = j
        if self._table[j] is None:
          return (False, firstAvail)
      elif k == self._table[j]._key:
        return (True, j)
      j = (j+1) % len(self._table)    # keep looking cyclically

  def _bucket_getitem(self, j, k):
    found, s = self._find_slot(j, k)
    if not found:
      raise KeyError('Key Error: ' + repr(k))
    return self._table[s]._value

  def _bucket_setitem(self, j, k, v):
    found, s = self._find_slot(j, k)
    if not found:
      self._table[j] = self._Item(k,v)
      self._n += 1
    else:
      self._table[s]._value = v

  def _bucket_delitem(self, j, k):
    found, s = self._find_slot(j, k)
    if not found:
      raise KeyError('Key Error: ' + repr(k))
    self._table[s] = ProbeHashMap._AVAIL

  def __iter__(self):
    for j in range(len(self._table)):
      if not self._is_available(j):
        yield self._table[j]._key