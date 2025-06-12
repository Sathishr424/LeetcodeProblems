# Last updated: 12/6/2025, 5:33:34 am
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        sums = []
        for i, num in enumerate(nums):
            tmp = num
            s = 0
            while num:
                s += num % 10
                num //= 10
            sums.append((s, tmp, i))
        
        new_sums = sorted(sums)
        indexes = {}

        for i in range(n):
            indexes[new_sums[i][2]] = i
        
        swap = 0
        i = 0
        while i < n:
            index = sums[i][2]
            if indexes[index] != i:
                sums[i], sums[indexes[index]] = sums[indexes[index]], sums[i]
                swap += 1
            else:
                i += 1
        
        return swap
        
        