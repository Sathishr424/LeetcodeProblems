# Last updated: 12/25/2025, 7:10:20 PM
class Solution:
    def maxBalancedShipments(self, weight: List[int]) -> int:
        # weight = [random.randrange(1, 10**9) for _ in range(10 ** 5)]
        n = len(weight)

        smallest = [-1] * n
        stack = []
        for i in range(n):
            while stack and weight[stack[-1]] <= weight[i]:
                stack.pop()
            if stack:
                smallest[i] = stack[-1]
            stack.append(i)
        
        @cache
        def rec(index):
            if index <= 0: return 0

            ans = rec(index - 1)
            if smallest[index] != -1:
                ans = max(ans, rec(smallest[index] - 1) + 1)

            return ans
        
        return rec(n-1)