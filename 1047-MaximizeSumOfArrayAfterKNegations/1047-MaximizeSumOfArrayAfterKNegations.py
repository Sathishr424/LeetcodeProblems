# Last updated: 12/6/2025, 5:44:28 am
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)

        index = 0
        leftSum = 0
        while index < n and k > 0 and nums[index] < 0:
            leftSum += -nums[index]
            index += 1
            k -= 1
        if index > 0:
            tmp = leftSum
            if k >= 1:
                if index < n:
                    tmp += -nums[index]
                else:
                    tmp += -float('inf')
                leftSum += nums[index-1]
                k += 1
                val = nums[index-1]
                for _ in range(k):
                    val = -val
                leftSum += val
                k = 0
                if tmp+sum(nums[index+1:]) > leftSum+sum(nums[index:]):
                    leftSum = tmp
                    index += 1
        if k > 0:
            val = nums[0]
            for _ in range(k):
                val = -val
            leftSum += val
            index += 1

        return leftSum + sum(nums[index:])
        
        
