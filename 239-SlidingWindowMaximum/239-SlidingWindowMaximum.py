# Last updated: 25/6/2025, 7:36:15 am
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        
        ret = []
        stack = deque([])
        for i in range(n):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
            stack.append(i)
            left = i - k + 1
            while stack and stack[0] < left:
                stack.popleft()

            if i >= k-1:
                ret.append(nums[stack[0]])

        return ret