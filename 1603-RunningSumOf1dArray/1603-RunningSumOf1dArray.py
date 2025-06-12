# Last updated: 12/6/2025, 5:41:21 am
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ret = []
        for i in range(len(nums)-1,-1,-1):
            cnt = 0
            for j in range(i,-1,-1):
                cnt += nums[j]
            ret.append(cnt)
        return ret[::-1]