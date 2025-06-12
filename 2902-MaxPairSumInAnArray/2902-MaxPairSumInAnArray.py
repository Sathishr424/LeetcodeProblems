# Last updated: 12/6/2025, 5:36:35 am
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        n = len(nums)
        ret = 0
        not_found = True
        for i in range(n-1):
            for j in range(i+1, n):
                t1 = max(str(nums[i]))
                t2 = max(str(nums[j]))
                if t1 == t2:
                    ret = max(ret, nums[i] + nums[j])
                    not_found = False
        return -1 if not_found else ret
        