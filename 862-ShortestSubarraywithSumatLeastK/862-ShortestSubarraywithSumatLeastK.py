# Last updated: 23/7/2025, 5:59:15 pm
cmin = lambda x, y: x if x < y else y
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)

        s = 0
        ret = n + 1
        stack = deque([(0, -1)])

        for i in range(n):
            s += nums[i]

            while stack and stack[-1][0] > s:
                stack.pop()
            
            stack.append((s, i))

            while stack and s - stack[0][0] >= k:
                c, p = stack.popleft()
                ret = cmin(ret, i - p)
        
        if ret == n + 1: return -1
        return ret