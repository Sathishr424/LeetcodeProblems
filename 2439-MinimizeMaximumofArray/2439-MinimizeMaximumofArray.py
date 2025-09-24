# Last updated: 25/9/2025, 2:32:28 am
class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        n = len(nums)

        def isGood(mid):
            can_remove = 0
            for i in range(n):
                num = nums[i]
                need = max(0, num - mid)
                if can_remove < need: return False
                can_remove -= need

                add = max(0, mid - num)
                can_remove += add

            return True
                
        l = 0
        r = max(nums)

        while l < r:
            mid = (l + r) // 2

            if isGood(mid):
                r = mid
            else:
                l = mid + 1

        return l