# General Tree
class GeneralTree:
  def __init__(self, value):
    self.value = value
    self.children = []

  def add_children(self, child_node):
    self.children.append(child_node)

  def remove_child(self, child_node):
    self.children.remove(child_node)


# Binary Tree
class BinaryTree:
  class Node:
    def __init__(self, value):
      self.value = value
      self.left = None
      self.right = None
      self.parent = None

  def add_left(self, child_node):
    if self.left is not None: raise ValueError('left child exists')
    self.left = child_node
    child_node.parent = self

  def add_right(self, child_node):
    if self.right is not None: raise ValueError('right child exists')
    self.right = child_node
    child_node.parent = self

  def replace(self, new):
    old = self.value
    self.value = new
    return old

  def num_children(self):
    count = 0
    if self.left is not None:
      count += 1
    if self.right is not None:
      count += 1
    return count

  def delete(self):
    if self.num_children() == 2: raise ValueError('the node has two children')
    child = self.left if self.left else self.right
    if self.parent:
      if self.parent.left is self:
        self.parent.left = child
      else:
        self.parent.right = child
    if child:
      child.parent = self.parent
    self.parent = self
    return self.value

  def attach(self, t1, t2):
    if not self.num_children() == 0: raise ValueError('node must be leaf')
    if t1:
      self.left = t1
      t1.parent = self
    if t2:
      self.right = t2
      t2.parent = self

root = BinaryTree.Node('A')
left = root.add_left('B')
left = BinaryTree('B')
right = BinaryTree('C')
root.attach(left, right)
root.delete()    # will cause a value error
left.delete()