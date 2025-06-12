# Last updated: 12/6/2025, 5:33:22 am
N = 10**5 + 1
mod = 10**9 + 7
fact = [1] * N

for i in range(1, N):
    fact[i] = i * fact[i-1] % mod

class Solution:
    def countPermutations(self, comp: List[int]) -> int:
        n = len(comp)

        sl = SortedList()
        sl.add(comp[0])

        cnts = [0] * n
        ret = 0
        
        for i in range(1, n):
            index = sl.bisect_left(comp[i])
            if index == 0: return 0
            sl.add(comp[i])

        return fact[n-1]