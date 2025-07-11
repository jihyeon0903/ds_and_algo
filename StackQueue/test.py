# Dynamic Array
class Array:
  def __init__(self):
    self.data = []
    self.size = 0
    self.capacity = 1

  def __len__(self):
    return self.size

  def append(self, e):
    if self.size == self.capacity:
      self.resize(2 * self.capacity)
    self.data[self.size] = e

  def insert(self, index, e):
    if self.size == self.capacity:
      self.resize(2 * self.capacity)
    for i in range(self.size, e, -1):
      self.data[i] = self.data[i-1]
    self.size += 1

  def remove(self, e):
    self.data[e] = None
    for k in range(e, self.size):
      self.data[k-1] = self.data[k]
    self.size -= 1

  def resize(self, cap):
    old = self.data
    self.data = [None] * cap
    for k in range(len(old)):
      self.data[k] = old[k]
    self.capacity = cap

# Stack
class ArrayStack:
  def __init__(self):
    self.data = []

  def __len__(self):
    return len(self.data)

  def is_empty(self):
    return len(self.data) == 0

  def __str__(self):
    return str(self.data)

  def push(self, e):
    return self.data.append(e)

  def pop(self):
    if self.is_empty():
      return "Stack is empty"
    return self.data.pop()

  def top(self):
    if self.is_empty():
      return "Stack is empty"
    return self.data[-1]

# S = ArrayStack()
# S.push(1)
# S.push(2)
# print(S.top())
# print(S.pop())
# print(S)

# Queue
class ArrayQueue:
  default_capacity = 10

  def __init__(self):
    self.data = [None] * ArrayQueue.default_capacity
    self.size = 0
    self.front = 0

  def __len__(self):
    return self.size

  def __str__(self):
    return str(self.data)

  def is_empty(self):
    return self.size == 0

  def dequeue(self):
    if self.is_empty():
      return "Queue is empty"
    self.data[self.front] = None
    self.front = (self.front + 1) % len(self.data)
    self.size -= 1

  def enqueue(self, e):
    if self.size == len(self.data):
      self.resize(2 * len(self.data))
    avail = (self.front + self.size) % len(self.data)
    self.data[avail] = e
    self.size += 1

  def resize(self, cap):
    old = self.data
    self.data = [None] * cap
    for k in range(len(old)):
      self.data[k] = old[k]
      self.front = (self.front + 1) % len(self.data)
    self.capacity = cap

# Q = ArrayQueue()
# Q.enqueue(1)
# Q.enqueue(4)
# Q.enqueue(8)
# Q.dequeue()
# Q.enqueue(1)
# print(Q)