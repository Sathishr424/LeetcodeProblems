# Last updated: 16/4/2025, 11:34:19 pm
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()

        p_index = bisect_left(nums, 1)
        if p_index == 0: return []

        index = 0

        ret = []
        if bisect_right(nums, 0) - bisect_left(nums, 0) >= 3: ret.append([0, 0, 0])

        pos = {}
        neg = {}
        for i in range(p_index, n):
            pos[nums[i]] = 1
        
        for i in range(0, p_index):
            if i > 0 and nums[i] == nums[i-1]: continue
            neg[nums[i]] = 1
            for j in range(i+1, p_index):
                if j > i+1 and nums[j] == nums[j-1]: continue
                s = -(nums[i]+nums[j])
                if s in pos:
                    ret.append([nums[i], nums[j], s])
        
        for i in range(p_index, n):
            if i > 0 and nums[i] == nums[i-1]: continue
            for j in range(i+1, n):
                if j > i+1 and nums[j] == nums[j-1]: continue
                s = -(nums[i]+nums[j])
                if s in neg:
                    ret.append([nums[i], nums[j], s])

        return ret


