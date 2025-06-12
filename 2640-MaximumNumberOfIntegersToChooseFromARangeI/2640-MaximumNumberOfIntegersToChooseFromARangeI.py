# Last updated: 12/6/2025, 5:37:25 am
class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        hash = {}
        for num in banned: hash[num] = 1
        cnt = 0
        total = 0
        for num in range(1, n+1):
            if num not in hash:
                total += num
                if total > maxSum: return cnt
                cnt += 1
        
        return cnt