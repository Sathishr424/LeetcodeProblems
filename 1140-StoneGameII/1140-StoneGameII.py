# Last updated: 8/9/2026, 2:12:29 PM
1class Solution:
2    def stoneGameII(self, piles: List[int]) -> int:
3        n = len(piles)
4        inf = 10**20
5
6        @cache
7        def rec(index, m, is_alice_turn):
8            if index == n: return 0
9            add = 1 if is_alice_turn else -1
10            compare = max if is_alice_turn else min
11
12            curr = 0
13            ans = inf * (-add)
14            for i in range(index, min(n, index + 2 * m)):
15                curr += piles[i]
16                ans = compare(ans, rec(i + 1, max(m, i - index + 1), not is_alice_turn) + curr * add)
17                # print((index, i), m, is_alice_turn, ans, 2 * m, (index, i, curr))
18
19            return ans
20
21        ans =  rec(0, 1, True)
22        rec.cache_clear()
23        return (sum(piles) + ans) // 2