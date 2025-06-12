# Last updated: 12/6/2025, 5:44:12 am
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        diffs = {}
        for i in range(n):
            for j in range(i+1,n):
                diff = nums[j] - nums[i]
                diffs[diff] = 1
        
        ret = 0
        for diff in diffs:
            hash = {}
            ans = 1
            for a in nums:
                d = a - diff
                if d in hash:
                    hash[a] = hash[d] + 1
                    ans = max(ans, hash[a])
                else: hash[a] = 1
            ret = max(ret, ans)
        return ret
        