# Last updated: 16/4/2025, 10:15:41 pm
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        n = len(nums)
        nums.sort()

        if nums[0] > 0: return []

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]: continue

            m = i+1
            r = n-1

            while m < r:
                t = nums[i] + nums[m] + nums[r]

                if t > 0:
                    r -= 1
                elif t < 0:
                    m += 1
                else:
                    ret.append([nums[i], nums[m], nums[r]])
                    # m += 1
                    r -= 1
                    # while m < r and nums[m] == nums[m-1]: m += 1
                    while r > m and nums[r] == nums[r+1]: r -= 1

        return ret