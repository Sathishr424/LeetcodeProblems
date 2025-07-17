# Last updated: 17/7/2025, 9:29:14 pm
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        def rec(index):
            cost = 0
            for i in position:
                dis = abs(i - index)
                cost += dis % 2
            return cost
        
        return min(rec(0), rec(1))