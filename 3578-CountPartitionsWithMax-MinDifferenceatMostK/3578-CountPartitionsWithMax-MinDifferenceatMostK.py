# Last updated: 25/6/2025, 7:16:23 am
inf = float('inf')
mod = 10 ** 9 + 7
class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        n = len(nums)
        sl = SortedList()
        prev = n-1
        comb = [0] * (n + 1)
        comb[n] = 1
        prefix = [0] * (n + 1)
        for i in range(n-1, -1, -1):
            sl.add(nums[i])

            while sl[-1] - sl[0] > k:
                sl.remove(nums[prev])
                prev -= 1
            
            prefix[i] = (prefix[i+1] + comb[i + 1]) % mod

            comb[i] = (prefix[i] - prefix[prev + 1]) % mod

        return comb[0]