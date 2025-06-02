# Last updated: 2/6/2025, 1:11:20 pm
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)

        left = [0] * n
        right = [0] * n

        cnt = 1
        for i in range(1, n):
            if ratings[i-1] >= ratings[i]:
                cnt = 0
            left[i] = cnt
            cnt += 1

        cnt = 1
        for i in range(n-2, -1, -1):
            if ratings[i+1] >= ratings[i]:
                cnt = 0
            right[i] = cnt
            cnt += 1

        ret = 0
        for i in range(n):
            ret += max(left[i], right[i]) + 1

        return ret