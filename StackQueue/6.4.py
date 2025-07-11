"""
Recursive method of removing all items in stack
"""

def recursiveDeletion(S: list):
  if len(S) == 0:
    return
  else:
    print(S)
    S.pop()
    recursiveDeletion(S)

recursiveDeletion([1,2,3,4,5])