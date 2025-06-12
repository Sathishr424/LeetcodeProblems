# Last updated: 12/6/2025, 5:48:20 am
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visited = [-1] * len(nums)
        def findLen(i):
            cnt = 0
            while True:
                if visited[i] != -1:
                    return
                cnt += 1
                visited[i] = cnt
                i = nums[i]
        maxi = 0
        for i in range(len(nums)):
            findLen(i)
        return max(visited)