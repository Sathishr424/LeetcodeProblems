# Last updated: 5/8/2025, 1:01:24 pm
N = 10 ** 5 + 1
is_prime = [1] * N
is_prime[0] = 0
is_prime[1] = 0
for i in range(2, int(N ** 0.5) + 1):
    if not is_prime[i]: continue
    for j in range(i * i, N, i):
        is_prime[j] = False
primes = []

for i in range(N):
    if is_prime[i]:
        primes.append(i)

class Union:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.sizes = [1] * n

    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])

        return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y: return True

        if self.sizes[y] > self.sizes[x]:
            x, y = y, x

        self.sizes[x] += self.sizes[y]
        self.parents[y] = x
        
        return False

class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        # nums = [randrange(1, N) for _ in range(10 ** 4 * 2)]
        n = len(nums)
        graph = {}
        un = Union(n)

        def link(p, index):
            print(p, index)
            if p in graph:
                un.union(graph[p], index)
            else:
                graph[p] = index
        

        there = {}
        for i, num in enumerate(nums):
            there[num] = i
        
        max_num = max(nums)
        for p in primes:
            num = p
            while num <= max_num:
                if num in there:
                    link(p, there[num])
                num += p

        # print(dict(graph))
        ret = 1
        for i in range(n):
            ret = max(ret, un.sizes[un.find(i)])
        # print(un.parents)
        return ret