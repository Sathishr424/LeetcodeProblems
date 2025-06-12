# Last updated: 12/6/2025, 5:52:23 am
class Node:
    def __init__(self, val, key, next=None, prev=None):
        self.val = val
        self.key = key
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.key_to_node = {}
        self.head = Node(-1, -1)
        self.last = self.head
        self.cap = capacity
        self.cnt = 0

    def get(self, key: int) -> int:
        if key in self.key_to_node:
            node = self.key_to_node[key]
            if self.last == node: return node.val
            prev = node.prev
            prev.next = node.next
            node.next.prev = prev
            self.last.next = Node(node.val, key, None, self.last)
            self.last = self.last.next
            self.key_to_node[key] = self.last
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            self.key_to_node[key].val = value
            self.get(key)
        else:
            if self.cnt == self.cap:
                node = self.head.next
                if self.cap == 1:
                    self.head.next = None
                    self.last = self.head
                else:
                    self.head.next = self.head.next.next
                    self.head.next.prev = self.head
                del self.key_to_node[node.key]
            else:
                self.cnt += 1
            self.last.next = Node(value, key, None, self.last)
            self.last = self.last.next
            self.key_to_node[key] = self.last

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)