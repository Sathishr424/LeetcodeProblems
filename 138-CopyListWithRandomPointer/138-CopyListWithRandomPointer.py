# Last updated: 12/6/2025, 5:52:30 am
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hash_random = {}
        hash_val = {}
        ret = Node(0)
        ret_head = ret
        while head:
            ret.next = Node(head.val)
            ret = ret.next
            hash_val[head] = ret
            if head.random: hash_random[ret] = head.random
            head = head.next
        
        for node in hash_random:
            node.random = hash_val[hash_random[node]]
        return ret_head.next