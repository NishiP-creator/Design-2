"""
Time Complexity:
put: 
get:
remove:
Space Complexity:
O(L) where L is the length of the linked list --> Ammortized O(1)
"""

class MyHashMap:

    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None

    def __init__(self):
        self.storage = [None] * 1001

    def getHash(self, key):
        return (2 * key) % 1001

    def getPrev(self, head, key):
        prev = None
        curr = head
        while curr and curr.key != key:
            prev = curr
            curr = curr.next
        return prev

    def put(self, key: int, value: int) -> None:
        index = self.getHash(key)
        if self.storage[index] is None:
            self.storage[index] = self.Node(-1, -1)
            self.storage[index].next = self.Node(key, value)
            return

        prev = self.getPrev(self.storage[index], key)
        if prev.next is None:
            prev.next = self.Node(key, value)
        else:
            prev.next.value = value

    def get(self, key: int) -> int:
        index = self.getHash(key)
        if self.storage[index] is None:
            return -1
        prev = self.getPrev(self.storage[index], key)
        if prev.next is None:
            return -1
        return prev.next.value

    def remove(self, key: int) -> None:
        index = self.getHash(key)
        if self.storage[index] is None:
            return
        prev = self.getPrev(self.storage[index], key)
        if prev.next is None:
            return
        prev.next = prev.next.next