# Last updated: 3/8/2025, 11:00:23 am
class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        ret = -inf

        left = [-inf] * n
        right = [-inf] * n

        i = n-1
        while i > 0:
            j = i
            s = 0
            maxi = -inf
            while j - 1 >= 0 and nums[j] > nums[j - 1]:
                j -= 1
                s += nums[j]
                maxi = max(s, maxi)
            if j != i:
                left[i] = maxi
            i = j
            i -= 1
            
        i = 0
        while i < n - 1:
            j = i
            s = 0
            maxi = -inf
            while j + 1 < n and nums[j] < nums[j + 1]:
                j += 1
                s += nums[j]
                maxi = max(s, maxi)
            
            if j != i:
                right[i] = maxi
            i = j
            i += 1

        i = 0
        while i < n - 1:
            j = i
            s = nums[i]
            while j + 1 < n and nums[j] > nums[j + 1]:
                j += 1
                s += nums[j]
            
            if j != i:
                ret = max(ret, s + left[i] + right[j])
            i = j
            i += 1
        
        return ret