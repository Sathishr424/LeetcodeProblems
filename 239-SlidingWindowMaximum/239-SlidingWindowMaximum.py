# Last updated: 25/6/2025, 7:38:38 am
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        
        stack = deque([])

        for i in range(k):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
            stack.append(i)
        
        ret = []
        ret.append(nums[stack[0]])
        for i in range(k, n):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
                
            stack.append(i)

            if stack[0] <= i - k:
                stack.popleft()

            ret.append(nums[stack[0]])

        return ret