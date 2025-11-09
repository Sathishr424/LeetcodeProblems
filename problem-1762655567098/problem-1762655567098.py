# Last updated: 9/11/2025, 8:02:47 am
class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        n = len(nums)

        min_dis = inf
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if nums[i] == nums[j] and nums[k] == nums[j]:
                        min_dis = min(min_dis, (j - i) + (k - j) + (k - i))

        return -1 if min_dis == inf else min_dis