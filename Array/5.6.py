import ctypes

class DynamicArray:
  def __init__(self):
    self.n = 0
    self.capacity = 1
    self.A = self.make_array(self.capacity)

  def __len__(self):
    return self.n

  def __getitem__(self, k):
    if not 0 <= k < self.n:
      raise IndexError('invalid index')
    return self.A[k]

  def append(self, obj):
    if self.n == self.capacity:
      self.resize(2*self.capacity)
    self.A[self.n] = obj
    self.n += 1

  def insert_and_resize(self, k, val):
    if self.n == self.capacity:
      B = self.make_array(2*self.capacity)
      for i in range(k):
        B[i] = self.A[i]
      B[k] = val
      for j in range(self.n, k, -1):
        B[j] = self.A[j-1]
      self.A = B
      self.capacity = 2*self.capacity
    self.n += 1

  def make_array(self, c):
    return (c * ctypes.py_object)()

lst = DynamicArray()
lst.append(7)
lst.insert_and_resize(0, 8)
print(lst[0])