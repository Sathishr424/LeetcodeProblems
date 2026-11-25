# Last updated: 11/25/2026, 12:21:13 PM
1N = 10**5
2mod = 10**9 + 7
3base = random.randint(N + 1, mod - 1)
4base_inverse = pow(base, -1, mod)
5
6powers = [1] * N
7curr = 1
8for i in range(1, N):
9    curr = (curr * base) % mod
10    powers[i] = curr
11
12class Solution:
13    def smallestUniqueSubarray(self, nums: List[int]) -> int:
14        n = len(nums)
15
16        def isGood(k):
17            found = defaultdict(int)
18            rolling = 0
19            for i in range(k):
20                rolling = (rolling + nums[i] * powers[i] % mod) % mod
21            found[rolling] += 1
22
23            for i in range(k, n):
24                rolling = (rolling - nums[i-k]) % mod * base_inverse % mod
25                rolling = (rolling + nums[i] * powers[k-1]  % mod) % mod
26                found[rolling] += 1
27
28            for roll in found:
29                if found[roll] == 1: return True
30
31            return False
32
33        l = 1
34        r = n
35        while l < r:
36            mid = (l + r) // 2
37
38            if isGood(mid):
39                r = mid
40            else:
41                l = mid + 1
42
43        return l