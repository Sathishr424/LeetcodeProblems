# Last updated: 12/6/2025, 5:33:46 am
class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        n = len(cost)
        ret = [0] * n
        ret[0] = cost[0]
        
        for i in range(1, n):
            if ret[i-1] < cost[i]:
                ret[i] = ret[i-1]
            else:
                ret[i] = cost[i]

        return ret