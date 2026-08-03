# Last updated: 8/3/2026, 8:58:01 PM
1class Solution:
2    def stoneGameIII(self, stoneValue: List[int]) -> str:
3        n = len(stoneValue)
4
5        @cache
6        def rec(index, turn):
7            add = 1 if turn else -1
8            if index == n:
9                return 0
10
11            compare = max if turn else min
12            curr = stoneValue[index]
13            ans = rec(index + 1, not turn) + curr * add
14            for i in range(index + 1, min(n, index + 3)):
15                curr += stoneValue[i]
16                ans = compare(ans, rec(i + 1, not turn) + curr * add)
17
18            return ans
19
20        ans = rec(0, True)
21        rec.cache_clear()
22        if ans > 0:
23            return "Alice"
24        elif ans < 0:
25            return "Bob"
26        return "Tie"