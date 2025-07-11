"""
init
len
getitem
append
resize
insert
remove
"""

class DynamicArray:
  def __init__(self):
    self.size = 0
    self.capacity = 1
    self.A = self.make_array(self.capacity)

  def __len__(self):
    return self.size

  def __getitem__(self, k):
    if not 0 <= k < self.size:
      return 'invalid index'
    return self.A[k]

  def append(self, obj):
    if self.size == self.capacity:
      self.resize(2 * self.capacity)
    self.A[self.size] = obj
    self.size += 1

  def resize(self, cap):
    new = self.make_array(cap)
    for k in range(self.size):
      new[k] = self.A[k]
    self.A = new
    self.capacity = cap

  def insert(self, k, val):
    # double the size if it reaches the max capacity
    if self.size == self.capacity:
      self.resize(2 * self.capacity)
    # make a room for new val at index k
    for j in range(self.size, k, -1):
      self.A[j] = self.A[j-1]
    self.A[k] = val
    self.size += 1

  def remove(self, val):
    # search for the val
    for k in range(self.size):
      if self.A[k] == val:
        # if found, overwrite it with the next one ...
        for j in range(k, self.size, -1):
          self.A[j] = self.A[j+1]
        self.A[self.size - 1] = None
        self.size -= 1
        return
    return 'value not found'
