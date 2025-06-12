# Last updated: 12/6/2025, 5:51:19 am
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1 = 0
        c2 = 0
        v1 = 0
        v2 = 0
        m = len(nums)//3
        
        for i in range(len(nums)):
            if c1 == nums[i]:
                v1 += 1
            elif c2 == nums[i]:
                v2 += 1
            elif v1 == 0:
                c1 = nums[i]
                v1 = 1
            elif v2 == 0:
                c2 = nums[i]
                v2 = 1
            else:
                v1 -= 1
                v2 -= 1
        
        ret = []
        v1 = 0
        v2 = 0
        for num in nums:
            if num == c1:
                v1 += 1
            elif num == c2:
                v2 += 1
        
        if v1 > m: ret.append(c1)
        if v2 > m: ret.append(c2)
        return ret