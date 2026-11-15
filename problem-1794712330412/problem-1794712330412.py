# Last updated: 11/15/2026, 8:42:10 AM
1class Solution:
2    def maxDifference(self, nums: list[int]) -> int:
3        n = len(nums)
4
5        @cache
6        def rec(index, alice) -> int:
7            if index == n: return 0
8
9            add = 1 if alice else -1
10            curr = nums[index] * add
11            turn_one = rec(index + 1, not alice if curr % 3 == 0 else alice) + curr
12
13            if index + 1 == n: return turn_one
14
15            curr = (nums[index] + nums[index + 1]) * add
16            turn_two = rec(index + 2, not alice if curr % 3 == 0 else alice) + curr
17
18            if alice:
19                return max(turn_one, turn_two)
20            else:
21                return min(turn_one, turn_two)
22
23        ans = rec(0, True)
24        rec.cache_clear()
25        return ans