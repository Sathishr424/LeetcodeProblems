# Last updated: 12/6/2025, 5:38:19 am
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefSum = []
        n = len(nums)
        curr = 0
        for num in nums:
            curr += num
            prefSum.append(curr)
        
        ret = 0

        for i in range(n-1):
            if prefSum[i] >= prefSum[n-1] - prefSum[i]: ret += 1
        
        return ret