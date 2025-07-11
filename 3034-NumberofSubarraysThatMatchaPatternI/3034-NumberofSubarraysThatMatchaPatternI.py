# Last updated: 11/7/2025, 11:16:49 pm
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

        ret = 0
        j = 0
        i = 1
        while i < n:
            if pattern[j] == 0:
                if nums[i] == nums[i-1]: 
                    j += 1
                    if j == m:
                        ret += 1
                        j = lps[j - 1]
                elif j > 0:
                    j = lps[j - 1]
                    continue
            elif pattern[j] == 1:
                if nums[i] > nums[i-1]: 
                    j += 1
                    if j == m: 
                        ret += 1
                        j = lps[j - 1]
                elif j > 0:
                    j = lps[j - 1]
                    continue
            else:
                if nums[i] < nums[i-1]: 
                    j += 1
                    if j == m: 
                        ret += 1
                        j = lps[j - 1]
                elif j > 0:
                    j = lps[j - 1]
                    continue
            i += 1
        return ret  