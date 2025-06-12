# Last updated: 12/6/2025, 5:33:50 am
class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        
        bit_count = len(bin(n)) - 2
        bit = (1 << bit_count) - 1
        maxi = n | bit

        add = n >= 3
        ret = n + add

        for x in range(maxi, n-1, -1):
            for num in range(n, 0, -1):
                val = x ^ num
                if val <= n:
                    if (val % 2 == 0 and val+1 <= n) or (val % 2 == 1 and val-1 >= 1):
                        return max(ret, x + add)

        return ret
        
        