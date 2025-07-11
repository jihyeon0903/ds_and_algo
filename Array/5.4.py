import ctypes

class DynamicArray:
  def __init__(self):
    self.n = 0
    self.capacity = 1
    self.A = self.make_array(self.capacity)

  def __len__(self):
    return self.n

  def __getitem__(self, k):
    """ Allow using negative indices with __getitem__ """
    # if not 0 <= k < self.n:
    #   raise IndexError('invalid index')
    # return self.A[k]
    if k > self.n:
      raise IndexError('invalid index')
    if k < 0:
      return self.A[self.n + k]
    return self.A[k]

  def append(self, obj):
    if self.n == self.capacity:
      self.resize(2*self.capacity)
    self.A[self.n] = obj
    self.n += 1

  def resize(self, c):
    B = self.make_array(c)
    for k in range(self.n):
      B[k] = self.A[k]
    self.A = B
    self.capacity = c

  def make_array(self, c):
    return (c * ctypes.py_object)()


lst = DynamicArray()
print(len(lst))
lst.append(7)
print(len(lst), lst[0])