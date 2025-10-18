# Last updated: 18/10/2025, 2:09:03 pm
class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k * 2 >= n: return n

        k_range = [i for i in range(-k, k+1)]
        used = {}
        nums.sort()

        for num in nums:
            l = 0
            r = len(k_range) - 1

            while l < r:
                mid = (l + r) // 2

                if (num + k_range[mid]) not in used:
                    r = mid
                else:
                    l = mid + 1
            
            if (num + k_range[l]) not in used:
                used[(num + k_range[l])] = 1

        return len(used)