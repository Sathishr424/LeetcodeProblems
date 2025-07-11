# Last updated: 11/7/2025, 11:24:38 pm
class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n = len(nums)
        m = len(pattern)

        lps = [0] * m
        j = 0
        for i in range(1, m):
            while pattern[i] != pattern[j] and j >= 1:
                j = lps[j - 1]
            
            if pattern[i] == pattern[j]:
                j += 1
                lps[i] = j
        def compare(x, y, p):
            if p == 1:
                return x > y
            elif p == -1:
                return x < y
            else:
                return x == y

        ret = 0
        j = 0
        for i in range(1, n):
            while j > 0 and not compare(nums[i], nums[i-1], pattern[j]): 
                j = lps[j - 1]
            if compare(nums[i], nums[i-1], pattern[j]):
                j += 1
                if j == m: 
                    ret += 1
                    j = lps[j - 1]

        return ret  