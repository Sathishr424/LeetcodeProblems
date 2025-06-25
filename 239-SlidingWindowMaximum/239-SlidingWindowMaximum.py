# Last updated: 25/6/2025, 7:35:35 am
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        
        ret = []
        stack = deque([])
        for i in range(n):
            while stack and stack[-1][0] < nums[i]:
                stack.pop()
            stack.append((nums[i], i))
            left = i - k + 1
            while stack and stack[0][1] < left:
                stack.popleft()

            if i >= k-1:
                ret.append(stack[0][0])

        return ret