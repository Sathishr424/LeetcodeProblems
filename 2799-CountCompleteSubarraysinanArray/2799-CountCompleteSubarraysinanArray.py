# Last updated: 31/7/2025, 5:39:52 pm
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        uniq_cnt = len(set(nums))
        ret = 0
        
        cnt = 0
        left = 0
        freq = [0] * 2001
        
        for i in range(n):
            freq[nums[i]] += 1
            if freq[nums[i]] == 1:
                cnt += 1

            while left <= i and cnt == uniq_cnt:
                ret += n - i
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    cnt -= 1
                left += 1

        return ret
                