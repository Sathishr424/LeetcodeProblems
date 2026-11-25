# Last updated: 11/25/2026, 12:17:02 PM
1class Solution:
2    def smallestUniqueSubarray(self, nums: List[int]) -> int:
3        n = len(nums)
4        mod = 10**9 + 7
5        base = random.randint(max(nums), mod - 1)
6        base_inverse = pow(base, -1, mod)
7        # base = 5
8
9        def isGood(k):
10            found = defaultdict(int)
11            rolling = 0
12            for i in range(k):
13                rolling = (rolling + nums[i] * pow(base, i, mod) % mod) % mod
14            found[rolling] += 1
15            base_power = pow(base, k-1, mod)
16            # print(k, nums[0:k], rolling)
17
18            for i in range(k, n):
19                rolling = (rolling - nums[i-k]) % mod * base_inverse % mod
20
21                rolling = (rolling + nums[i] * base_power  % mod) % mod
22                found[rolling] += 1
23                # print(k, nums[i-k+1:i+1], rolling)
24
25            # print(k, dict(found))
26            for roll in found:
27                if found[roll] == 1: return True
28
29            return False
30
31        l = 1
32        r = n
33
34        while l < r:
35            mid = (l + r) // 2
36
37            if isGood(mid):
38                r = mid
39            else:
40                l = mid + 1
41
42        return l