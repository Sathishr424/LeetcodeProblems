# Last updated: 18/6/2025, 5:34:08 pm
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        n = len(nums)
        if n == 1: return []

        m = n // 3

        nums.sort()
        ret = []
        for i in range(m):
            start = i * 3
            end = start + 2
            if nums[end] - nums[start] > k: return []
            curr = []
            for j in range(start, end+1):
                curr.append(nums[j])
            ret.append(curr)

        return ret
                