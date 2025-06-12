# Last updated: 12/6/2025, 5:49:41 am
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2: return 0
        ret = 0
        cnt = 2
        prev = nums[1] - nums[0]
        for i in range(2, n):
            if nums[i] - nums[i-1] == prev:
                cnt += 1
            else:
                if cnt >= 3:
                    ret += cnt-2
                    cnt -= 3
                    ret += cnt*(cnt+1)//2
                cnt = 2
                prev = nums[i] - nums[i-1]
        if cnt >= 3:
            ret += cnt-2
            cnt -= 3
            ret += cnt*(cnt+1)//2
        return ret