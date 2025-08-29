# Last updated: 29/8/2025, 1:17:36 pm
class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        even = m // 2
        odd = m - even
        
        return (n // 2) * odd + ((n + 1) // 2) * even