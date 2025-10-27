# Last updated: 28/10/2025, 1:26:36 am
class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned.sort()

        index = 0
        cnt = 0
        for num in range(1, n+1):
            while index < len(banned) and num > banned[index]:
                index += 1
            if index >= len(banned) or num != banned[index]:
                if num > maxSum: break
                maxSum -= num
                cnt += 1
        
        return cnt
            