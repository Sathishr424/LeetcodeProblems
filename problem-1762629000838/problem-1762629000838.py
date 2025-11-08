# Last updated: 9/11/2025, 12:40:00 am
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)

        leftSum = [0] * n
        s = 0
        for i in range(n):
            leftSum[i] = s
            s += nums[i]

        rightSum = [0] * n
        s = 0
        for i in range(n-1, -1, -1):
            rightSum[i] = s
            s += nums[i]

        ret = []
        for i in range(n):
            ret.append(abs(leftSum[i] - rightSum[i]))

        return ret