# Last updated: 28/10/2025, 1:25:29 am
class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)

        cnt = 0
        for num in range(1, n+1):
            if num not in banned:
                if num > maxSum: break
                maxSum -= num
                cnt += 1
        
        return cnt
            