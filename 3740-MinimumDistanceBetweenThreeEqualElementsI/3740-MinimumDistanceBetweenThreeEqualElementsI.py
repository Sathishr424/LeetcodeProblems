# Last updated: 9/11/2025, 9:34:51 am
cmax = lambda x, y: x if x > y else y
cmin = lambda x, y: x if x < y else y
class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        n = len(nums)

        indexes = defaultdict(list)
        min_dis = inf
        for index, num in enumerate(nums):
            curr = indexes[num]
            curr.append(index)
            if len(curr) >= 3:
                i, j, k = curr[-3:]
                min_dis = cmin(min_dis, (j - i) + (k - j) + (k - i))

        return -1 if min_dis == inf else min_dis