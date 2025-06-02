# Last updated: 2/6/2025, 1:04:14 pm
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)

        left = [0] * n
        right = [0] * n

        stack = [ratings[0]]
        for i in range(1, n):
            if stack and stack[-1] >= ratings[i]:
                stack = []
            left[i] = len(stack)
            stack.append(ratings[i])

        stack = [ratings[-1]]
        for i in range(n-2, -1, -1):
            if stack and stack[-1] >= ratings[i]:
                stack = []
            right[i] = len(stack)
            stack.append(ratings[i])

        ret = 0
        for i in range(n):
            ret += max(left[i], right[i]) + 1

        return ret