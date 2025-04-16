# Last updated: 16/4/2025, 6:07:17 pm
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        s = 0

        uniq = defaultdict(int)
        uniq_cnt = 0
        
        for i in range(k):
            s += nums[i]
            uniq[nums[i]] += 1
            if uniq[nums[i]] == 1: uniq_cnt += 1
        
        ret = s if uniq_cnt == k else 0

        for i in range(k, len(nums)):
            uniq[nums[i-k]] -= 1
            if uniq[nums[i-k]] == 0:
                uniq_cnt -= 1
            
            s -= nums[i-k]
            s += nums[i]

            uniq[nums[i]] += 1
            if uniq[nums[i]] == 1:
                uniq_cnt += 1

            ret = max(s, ret) if uniq_cnt == k else ret
        
        return ret
