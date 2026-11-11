# Last updated: 11/11/2026, 1:55:16 PM
1class Solution:
2    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
3        if cost1 + cost2 < costBoth:
4            return need1 * cost1 + need2 * cost2
5        mn = min(need1, need2)
6        ans = mn * costBoth + (need1 - mn) * cost1 + (need2 - mn) * cost2
7        return min(ans, max(need1, need2) * costBoth)