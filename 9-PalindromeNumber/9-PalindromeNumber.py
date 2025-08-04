# Last updated: 4/8/2025, 11:19:54 pm
N = 101
fact = [1] * N
for i in range(1, N):
    fact[i] = fact[i - 1] * i

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq = [0] * 101

        for num in nums:
            freq[num] += 1

        ret = 0
        for cnt in freq:
            if cnt > 1:
                ret += fact[cnt] // (fact[2] * fact[cnt - 2])
        
        return ret