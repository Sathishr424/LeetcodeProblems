# Last updated: 15/7/2025, 5:51:44 pm
class Node:
    def __init__(self, val, prev=None):
        self.val = val
        self.prev = prev
        self.next = None
        self.deleted = False
        self.index = -1
    
    def __lt__(self, node):
        return self.index < node.index
    
    def __repr__(self):
        node = self
        st = ''
        while node:
            st += str(node.val) + f"({node.index})" +  ' -> '
            node = node.next
        return st

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        head = Node(nums[0])
        node = head
        node.index = 0

        heap = []
        bad_pairs = 0

        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                bad_pairs += 1
            node.next = Node(nums[i + 1], node)
            heapq.heappush(heap, (nums[i] + nums[i+1], node))
            node = node.next
            node.index = i + 1
        
        op = 0
        while bad_pairs:
            while heap and (heap[0][1].deleted or heap[0][1].val + heap[0][1].next.val != heap[0][0]):
                heapq.heappop(heap)
            s, node = heapq.heappop(heap)

            index = node.index
            # print('==>', s, node)
            node.deleted = True
            node.next.deleted = True

            new_node = Node(s, node.prev)
            new_node.index = index
            
            if node.prev:
                node.prev.next = new_node
                heapq.heappush(heap, (new_node.prev.val + new_node.val, new_node.prev))
                if node.val < node.prev.val:
                    if new_node.val >= new_node.prev.val: bad_pairs -= 1
                elif new_node.val < new_node.prev.val:
                    bad_pairs += 1
            else:
                head = new_node

            if node.val > node.next.val:
                bad_pairs -= 1

            if node.next.next:
                node.next.next.prev = new_node
                new_node.next = node.next.next

                heapq.heappush(heap, (new_node.val + new_node.next.val, new_node))

                if node.next.val > node.next.next.val:
                    if new_node.val <= new_node.next.val:
                        bad_pairs -= 1
                elif new_node.val > new_node.next.val:
                    bad_pairs += 1

            op += 1
        
        return op


            
