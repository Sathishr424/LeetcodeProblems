# Last updated: 12/6/2025, 5:51:09 am
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stack = deque([])

        n = len(nums)

        for i in range(k):
            num = nums[i]

            while stack and stack[-1] < num:
                stack.pop()
            stack.append(num)
        ret = [stack[0]]

        for i in range(k, n):
            num = nums[i]

            if stack[0] == nums[i-k]: stack.popleft()

            while stack and stack[-1] < num:
                stack.pop()
            stack.append(num)

            ret.append(stack[0])
        
        return ret