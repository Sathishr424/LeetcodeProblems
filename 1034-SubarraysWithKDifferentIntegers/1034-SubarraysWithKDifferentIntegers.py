# Last updated: 12/6/2025, 5:44:37 am
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ret = 0

        uniq = [0] * (n+1)
        matches = 0
        left = 0
        prev = 0

        cnts = [0] * (n+1)
        cnt_matches = 0
        cnt_left = 0

        for i in range(n):
            cnts[nums[i]] += 1
            if cnts[nums[i]] == 1: cnt_matches += 1

            if cnt_matches > k:
                while cnt_left < i and cnt_matches > k:
                    num = nums[cnt_left]
                    cnts[num] -= 1
                    if cnts[num] == 0: cnt_matches -= 1
                    cnt_left += 1
                prev = 0
            
            uniq[nums[i]] += 1
            if uniq[nums[i]] == 1: matches += 1

            if matches == k:
                while left <= i and matches == k:
                    num = nums[left]
                    uniq[num] -= 1
                    if uniq[num] == 0: matches -= 1
                    left += 1
                    prev += 1
 
            ret += prev
        
        return ret
        