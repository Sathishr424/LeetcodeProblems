# Last updated: 6/7/2025, 10:24:50 pm
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        stack = []
        smallest = [-1] * n
        for i in range(n-1, -1, -1):
            while stack and nums[i] <= nums[stack[-1]]:
                stack.pop()
            if stack:
                smallest[i] = stack[-1]
            stack.append(i)
            # print(nums[i], stack)
        # print(smallest)

        ret = []
        for i in range(n):
            if smallest[i] != -1 and n - smallest[i] + len(ret) >= k:
                continue
            ret.append(nums[i])
            if len(ret) == k: break

        return ret