# Last updated: 22/11/2025, 3:51:08 am
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.head = None
        self.tail = None
        self.size = 0
        self.cap = capacity
        self.keys = {}
    
    def removeNode(self, node):
        if node.prev and node.next:
            node.prev.next = node.next
            node.next.prev = node.prev
        elif node.prev:
            node.prev.next = None
            self.tail = node.prev
        elif node.next:
            node.next.prev = None
            self.head = node.next
        else:
            self.head = None
            self.tail = None
        node.next = None
        node.prev = None

    def addToTop(self, new_node):
        if self.head:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def get(self, key: int) -> int:
        if key in self.keys:
            node = self.keys[key]
            self.removeNode(node)
            self.addToTop(node)
            return self.keys[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.keys:
            new_node = Node(key, value)
            if self.size == self.cap:
                del self.keys[self.tail.key]
                self.removeNode(self.tail)
                self.size -= 1
            self.keys[key] = new_node
            self.size += 1
        else:
            self.removeNode(self.keys[key])
            self.keys[key].val = value
        self.addToTop(self.keys[key])

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)