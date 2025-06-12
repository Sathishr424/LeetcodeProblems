# Last updated: 12/6/2025, 5:41:43 am
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        m = len(nums)
        n = max([len(nums[i]) for i in range(m)])

        ans = [[] for _ in range(m+n-1)]

        for i in range(m-1, -1, -1):
            for j in range(len(nums[i])):
                ans[i+j].append(nums[i][j])

        ret = []
        for row in ans:
            for col in row:
                ret.append(col)
        
        return ret