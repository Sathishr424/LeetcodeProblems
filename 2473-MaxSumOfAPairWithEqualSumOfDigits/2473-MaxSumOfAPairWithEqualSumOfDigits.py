# Last updated: 12/6/2025, 5:37:53 am
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        memo = defaultdict(int)
        ret = -1
        for i in range(len(nums)):
            num = nums[i]

            cnt = 0
            while num:
                rem = num % 10
                num //= 10
                cnt += rem
            if cnt in memo:
                ret = max(ret, memo[cnt] + nums[i])
            memo[cnt] = max(memo[cnt], nums[i])
        
        return ret