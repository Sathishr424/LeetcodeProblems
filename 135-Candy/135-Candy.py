# Last updated: 2/6/2025, 1:14:22 pm
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)

        candies = [0] * n

        cnt = 1
        for i in range(1, n):
            if ratings[i-1] >= ratings[i]:
                cnt = 0
            candies[i] = cnt
            cnt += 1

        cnt = 1
        ret = candies[-1] + 1
        for i in range(n-2, -1, -1):
            if ratings[i+1] >= ratings[i]:
                cnt = 0
            candies[i] = max(candies[i], cnt)
            ret += candies[i] + 1
            cnt += 1

        return ret