# Last updated: 12/6/2025, 5:46:29 am
class Node:
    def __init__(self, key, value, _next=None):
        self.key = key
        self.value = value
        self.next = _next

class MyHashMap:
    def __init__(self):
        self.arr = [None for _ in range(256)]
    
    def _hash(self, key):
        index = 0
        for k in str(key):
            index += ord(k)
        return index % 256

    def _insert_to_node(self, node, key, value):
        if node.key == key:
            node.value = value
        elif node.next != None:
            node.next = self._insert_to_node(node.next, key, value)
        else: 
            node.next = Node(key, value)
        return node
    
    def _delete_from_node(self, node, key):
        if key == node.key: return node.next
        elif node.next != None:
            node.next = self._delete_from_node(node.next, key)
        return node
        
    def _get_from_node(self, node, key):
        if node.key == key: return node.value
        elif node.next != None: return self._get_from_node(node.next, key)
        return -1

    def put(self, key: int, value: int) -> None:
        index = self._hash(key)
        if self.arr[index] == None:
            self.arr[index] = Node(key, value)
        else: self.arr[index] = self._insert_to_node(self.arr[index], key, value)

    def get(self, key: int) -> int:
        index = self._hash(key)
        if self.arr[index] == None: return -1
        return self._get_from_node(self.arr[index], key)

    def remove(self, key: int) -> None:
        index = self._hash(key)
        if self.arr[index] == None: return
        self.arr[index] = self._delete_from_node(self.arr[index], key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)