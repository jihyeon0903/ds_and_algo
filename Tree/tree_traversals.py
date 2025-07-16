# preorder
class PreorderTraversal:
  """
  GENERATORS:
  normal function --> use the return keyword to return the values
  generator function --> instead of using the return, we use yield to execute the iterator
  """
  def preorder(self):
    if not self.is_empty():
      for p in self._subtree_preorder(self.root()):
        """
        YILED: Unlike the return keyword which stops further execution of the function,
        the yield keyword continues to the end of the function.
        The return value will be a list of values, one for each yield .
        """
        yield p

  def _subtree_preorder(self, p):
    yield p
    for c in self.children(p):
      for other in self._subtree_preorder(c):
        yield other

  def positions(self):
    return self.preorder()



# postorder
class PostorderTraversal:
  def postorder(self):
    if not self.is_empty():
      for p in self._subtree_postorder(self.root()):
        yield p

  def _subtree_postorder(self, p):
    for c in self.children(p):
      for other in self._subtree_postorder(c):
        yield other
    yield p

  def positions(self):
    return self.postorder()



# breadth-first
from LinkedList.linked_queue import LinkedQueue
def breadthfirst(self):
  if not self.is_empty():
    fringe = LinkedQueue()
    fringe.enqueue(self.root())
    while not fringe.is_empty():
      p = fringe.dequeue()
      yield p
      for c in self.children(p):
        fringe.enqueue(c)



# inorder
class InorderTraversal:
  def inorder(self):
    if not self.is_empty():
      for p in self._subtree_inorder(self.root()):
        yield p

  def _subtree_inorder(self, p):
    if self.left(p) is not None:
      for other in self._subtree_inorder(self.left(p)):
        yield other
    yield p
    if self.right(p) is not None:
      for other in self._subtree_inorder(self.right(p)):
        yield other

  def positions(self):
    return self.inorder()