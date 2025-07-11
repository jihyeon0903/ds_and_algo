"""
Implement the function transfer(S, T) --> transfers all elements from stack S onto stack T, reverse the order
"""

def transfer(S: list, T: list):
  while len(S) > 0:
    item = S.pop()
    T.append(item)
  return T

print(transfer([1,2,3,4,5], []))