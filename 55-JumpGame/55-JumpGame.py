# Last updated: 25/6/2025, 12:22:48 am
inf = float('inf')
cmin = lambda x, y: x if x < y else y

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [inf] * n
        dp[0] = 0

        stack = deque([])

        for i in range(n):
            while stack and stack[0] < i:
                stack.popleft()
            
            if stack: dp[i] = cmin(dp[i], dp[stack[0]])
            
            if nums[i]:
                index = cmin(n - 1, i + nums[i])
                dp[index] = cmin(dp[index], dp[i] + 1)
                while stack and stack[-1] < index and dp[stack[-1]] > dp[index]:
                    stack.pop()
                
                if not stack or stack[-1] < index:
                    stack.append(index)
        
        return dp[n-1]