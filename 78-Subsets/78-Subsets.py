# Last updated: 12/6/2025, 5:53:48 am
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        vis = {}
        def helper(index, num, dummy=""):
            nonlocal ret, vis
            if dummy not in vis: ret.append(num)
            vis[dummy] = True
            if index >= len(nums): return
            helper(index+1, num, dummy)
            helper(index+1, num + [nums[index]], dummy + "," + str(nums[index]))
        helper(0, [])
        return ret