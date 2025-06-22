"""
Time Complexity:
put: 
get:
remove:
Space Complexity:
O(L) where L is the length of the linked list --> Ammortized O(1)
"""

class MyHashMap():
  class Node():
    def __init__(self, key, value):
      self.key = key
      self.value = value
      self.next = None
  
  
  def __init__(self):
    self.storage = [None] * 1001
    
  
  def find(self, dummy, key):
    prev = None
    curr = dummy
    while curr and curr.key != key:
      prev = curr;
      curr = curr.next
    return prev
  
  
  def put(self, key, value):
    bucket = hash(key)%1000
    if self.storage[bucket] is None:
      self.storage[bucket] = self.Node(-1, -1)
      self.storage[bucket].next = self.Node(key, value)
      return
    
    prev = self.find(self.storage[bucket], key)
    if prev.next is None:
        prev.next = self.Node(key, value)
    else:
        prev.next.value = value


  def get(self, key: int) -> int:
      bucket = hash(key)%1000
      if self.storage[bucket] is None:
          return -1
      prev = self.find(self.storage[bucket], key)
      if prev.next is None:
          return -1
      return prev.next.value


  def remove(self, key: int) -> None:
      bucket = hash(key)%1000
      if self.storage[bucket] is None:
          return
      prev = self.find(self.storage[bucket], key)
      if prev.next is None:
          return
      prev.next = prev.next.next