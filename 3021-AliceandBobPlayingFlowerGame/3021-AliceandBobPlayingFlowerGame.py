# Last updated: 29/8/2025, 1:16:48 pm
class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        ret = 0
        even = m // 2
        odd = m - even
        for i in range(1, n + 1):
            if i % 2:
                ret += even
            else:
                ret += odd
        
        return ret