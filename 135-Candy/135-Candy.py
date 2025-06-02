# Last updated: 2/6/2025, 1:08:23 pm
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)

        left = [0] * n
        right = [0] * n

        stack = [1, ratings[0]]
        for i in range(1, n):
            if stack[-1] >= ratings[i]:
                stack = [0, -1]
            left[i] = stack[0]
            stack[0] += 1
            stack[-1] = ratings[i]

        stack = [1, ratings[-1]]
        for i in range(n-2, -1, -1):
            if stack[-1] >= ratings[i]:
                stack = [0, -1]
            right[i] = stack[0]
            stack[0] += 1
            stack[-1] = ratings[i]

        ret = 0
        for i in range(n):
            ret += max(left[i], right[i]) + 1

        return ret