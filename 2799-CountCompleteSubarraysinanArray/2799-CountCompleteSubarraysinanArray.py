# Last updated: 24/4/2025, 10:01:51 am
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        ret = 0

        uniq = {}
        for num in nums: uniq[num] = 1
        cnt = len(uniq)

        uniq = defaultdict(int)
        left = 0
        prev = 0

        for i in range(n):
            uniq[nums[i]] += 1
            
            if len(uniq) == cnt:
                while left <= i and len(uniq) == cnt:
                    prev += 1
                    uniq[nums[left]] -= 1
                    if uniq[nums[left]] == 0: del uniq[nums[left]]
                    left += 1
            ret += prev
        
        return ret