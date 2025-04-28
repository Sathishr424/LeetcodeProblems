# Last updated: 28/4/2025, 8:55:05 pm
class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        cuts = [0]
        """
        [3,4,5,6,7,8,8] 1
        """
        for i in range(1, n):
            if nums[i] - nums[i-1] > maxDiff:
                cuts.append(i)
        # print(cuts)
        ans = []
        for ui, vi in queries:
            x = bisect.bisect_right(cuts, ui)
            y = bisect.bisect_right(cuts, vi)
            ans.append(x == y)
        return ans