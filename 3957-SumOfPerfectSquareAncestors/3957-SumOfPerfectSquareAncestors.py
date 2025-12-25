# Last updated: 12/25/2025, 7:10:10 PM
N = 10**5 + 1
is_prime = [1] * N
is_prime[0] = 0
is_prime[1] = 0

for i in range(2, int(N ** 0.5) + 1):
    if not is_prime[i]: continue
    for j in range(i * i, N, i):
        is_prime[j] = 0
        
primes = []
for i in range(N):
    if is_prime[i]:
        primes.append(i)

@cache
def strip(num):
    s = 1
    for p in primes:
        if p > num: return s
        if num % p == 0:
            cnt = 0
            while num % p == 0:
                num //= p
                cnt += 1
            if cnt % 2: s *= p

    return s

class Solution:
    def sumOfAncestors(self, n: int, edges: List[List[int]], nums: List[int]) -> int:
        graph = defaultdict(list)

        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        ancestors = defaultdict(int)
        ans = 0
        def dfs(x, par):
            nonlocal ans
            val = strip(nums[x])
            # print(x, val, ancestors)
            ans += ancestors[val]
            ancestors[val] += 1
            for y in graph[x]:
                if y == par: continue
                dfs(y, x)
            ancestors[val] -= 1
        
        dfs(0, -1)
        return ans