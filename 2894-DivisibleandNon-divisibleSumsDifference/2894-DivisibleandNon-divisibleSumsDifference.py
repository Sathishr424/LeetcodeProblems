# Last updated: 27/5/2025, 5:53:00 am
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num = 0
        s = 0
        for i in range(1, n+1):
            s += i
            if i % m: num += i
        
        return num - (s - num)