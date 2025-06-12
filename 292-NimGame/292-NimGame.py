# Last updated: 12/6/2025, 5:50:49 am
class Solution:
    def canWinNim(self, n: int) -> bool:
        if n % 4 == 0: return False
        return True