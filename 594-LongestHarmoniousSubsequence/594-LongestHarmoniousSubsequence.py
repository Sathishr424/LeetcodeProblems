# Last updated: 12/6/2025, 5:48:13 am
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        n = len(nums)

        hash = defaultdict(int)
        ret = 0
        for num in nums:
            hash[num] += 1
        
        for num in nums:
            if hash[num+1]:
                ret = max(ret, hash[num+1] + hash[num])
        return ret