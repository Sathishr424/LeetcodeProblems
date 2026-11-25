# Last updated: 11/25/2026, 12:20:18 PM
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
22            # print(k, nums[0:k], rolling)
23
24            for i in range(k, n):
25                rolling = (rolling - nums[i-k]) % mod * base_inverse % mod
26
27                rolling = (rolling + nums[i] * powers[k-1]  % mod) % mod
28                found[rolling] += 1
29                # print(k, nums[i-k+1:i+1], rolling)
30
31            # print(k, dict(found))
32            for roll in found:
33                if found[roll] == 1: return True
34
35            return False
36
37        l = 1
38        r = n
39
40        while l < r:
41            mid = (l + r) // 2
42
43            if isGood(mid):
44                r = mid
45            else:
46                l = mid + 1
47
48        return l