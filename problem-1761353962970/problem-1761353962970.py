# Last updated: 25/10/2025, 6:29:22 am
class Solution:
    def totalMoney(self, n: int) -> int:
        prev_monday = 0
        total = 0
        prev = 0
        for i in range(n):
            if i % 7 == 0:
                curr = prev_monday + 1
                prev_monday = curr
                prev = curr
            else:
                prev += 1
            total += prev
        
        return total
            