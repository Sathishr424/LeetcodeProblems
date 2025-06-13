# Last updated: 13/6/2025, 9:03:26 am
class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        n = len(nums)
        nums.sort()

        l = 0
        r = (nums[-1] - nums[0]) + 1

        while l < r:
            mid = (l + r) // 2

            start = 0
            cnt = 0
            for i in range(1, n):
                if nums[i] - nums[start] > mid:
                    diff = i - start
                    cnt += diff // 2
                    if diff % 2 == 0 or nums[i] - nums[i-1] > mid:
                        start = i
                    else:
                        start = i-1
            
            cnt += (n - start) // 2

            if cnt >= p:
                r = mid
            else:
                l = mid + 1
        
        return l