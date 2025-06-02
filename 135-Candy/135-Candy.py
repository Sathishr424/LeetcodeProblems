# Last updated: 2/6/2025, 1:03:33 pm
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n

        """
        [1, 0, 2, 3, 1, 2, 3, 4, 2, 1, 0]
        [2, 1, 2, 3, 1, 2, 3, 4, 2]
        """
        
        stack = [ratings[0]]
        left = [0] * n
        right = [0] * n

        for i in range(1, n):
            # print(stack)
            if stack and stack[-1] >= ratings[i]:
                stack = []
            left[i] = len(stack)
            stack.append(ratings[i])

        stack = [ratings[-1]]
        for i in range(n-2, -1, -1):
            # print(stack)
            if stack and stack[-1] >= ratings[i]:
                stack = []
            right[i] = len(stack)
            stack.append(ratings[i])
                
        # print(stack)
        # print()
        # print(ratings)
        # print(left)
        # print(right)

        for i in range(n):
            candies[i] = max(left[i], right[i]) + 1

        return sum(candies)