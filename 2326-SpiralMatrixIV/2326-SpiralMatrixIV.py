# Last updated: 17/9/2025, 9:00:48 pm
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        grid = [[-1] * n for _ in range(m)]

        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        node = head
        i = 0
        j = 0
        d = 0
        while node:
            grid[i][j] = node.val
            if node.next == None: break
            i2 = i + direction[d][0]
            j2 = j + direction[d][1]
            
            if 0 <= i2 < m and 0 <= j2 < n and grid[i2][j2] == -1:
                i = i2
                j = j2
                node = node.next
            else:
                d = (d + 1) % 4

        return grid