# Last updated: 12/6/2025, 5:40:01 am
class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)

        rotate = -1
        mini = nums[0]

        for i in range(1, n):
            if nums[i-1] > nums[i]: 
                rotate = i
                break
            mini = min(mini, nums[i])

        if rotate != -1:
            if nums[rotate] > mini: return False
            for i in range(rotate+1, n):
                if nums[i] < nums[i-1] or nums[i] > mini: return False

        return True