# Last updated: 12/6/2025, 5:36:47 am
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        ret = 0

        uniq = {}
        for num in nums: uniq[num] = 1
        cnt = len(uniq)

        uniq = [0] * 2001
        matches = 0
        left = 0
        prev = 0

        for i in range(n):
            uniq[nums[i]] += 1
            if uniq[nums[i]] == 1: matches += 1
            
            if matches == cnt:
                while left <= i and matches == cnt:
                    prev += 1
                    uniq[nums[left]] -= 1
                    if uniq[nums[left]] == 0: matches -= 1
                    left += 1
            ret += prev
        
        return ret