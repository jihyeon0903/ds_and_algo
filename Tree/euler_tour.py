class EulerTour:
  # abstract base class
  def __init__(self, tree):
    self._tree = tree

  def tree(self):
    # reference to the tree being traversed
    return self._tree

  def execute(self):
    if len(self._tree) > 0:
      return self._tour(self._tree.root(), 0 , [])

  def tour(self, p, d, path):
    """
    p: position of current node being visited
    d: depth of p in the tree
    path: list of indices of children on path from root to p
    """
    self._hook_previsit(p, d, path)
    result = []
    # add new index to the end of path before recursion
    path.append(0)
    for c in self._tree.children(p):
      # recur on child's subtree
      result.append(self._tour(c, d+1, path))
      # increment index
      path[-1] += 1
    path.pop()
    answer = self._hook_postvisit(p, d, path, result)
    return answer

  def _hook_previsit(self, p, d, path):
    pass

  def _hook_postvisit(self, p, d, path, results):
    pass