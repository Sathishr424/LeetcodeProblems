# Last updated: 27/8/2025, 10:16:09 pm
class DLinkedList:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        head = DLinkedList(nums[0])
        node = head
        for i in range(1, len(nums)):
            dl = DLinkedList(nums[i])
            dl.prev = node
            node.next = dl
            node = node.next

        node = head
        while node.next:
            if gcd(node.val, node.next.val) > 1:
                new_dl = DLinkedList(lcm(node.val, node.next.val))
                prev = node.prev
                next = node.next.next
                new_dl.prev = prev
                new_dl.next = next
                if next:
                    next.prev = new_dl
                
                if prev:
                    prev.next = new_dl
                    node = prev
                else:
                    head = new_dl
                    node = new_dl
                continue
            node = node.next

        ret = []
        while head:
            ret.append(head.val)
            head = head.next

        return ret 