# Last updated: 24/4/2025, 10:51:31 am
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ret = 0

        uniq = defaultdict(int)
        left = 0
        prev = 0
        
        cnts = defaultdict(int)
        cnts_left = 0

        for i in range(n):
            cnts[nums[i]] += 1

            if len(cnts) > k:
                while cnts_left < i and len(cnts) > k:
                    num = nums[cnts_left]
                    cnts[num] -= 1
                    if cnts[num] == 0: del cnts[num]
                    cnts_left += 1
                prev = 0
            
            uniq[nums[i]] += 1

            if len(uniq) == k:
                while left <= i and len(uniq) == k:
                    prev += 1
                    uniq[nums[left]] -= 1
                    if uniq[nums[left]] == 0: del uniq[nums[left]]
                    left += 1
 
            ret += prev

            # print(nums[left:i+1], dict(uniq), ret, prev, dict(cnts))
        
        return ret
        