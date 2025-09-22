# Last updated: 23/9/2025, 3:27:20 am
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        ret = []
        stack = deque([])
        for i in range(k):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()

            stack.append(i)
        
        ret.append(nums[stack[0]])

        for i in range(k, n):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()

            stack.append(i)

            while stack and stack[0] <= i - k:
                stack.popleft()
            
            ret.append(nums[stack[0]])
        
        return ret