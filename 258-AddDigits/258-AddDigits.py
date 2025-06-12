# Last updated: 12/6/2025, 5:51:05 am
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0: return 0
        return 9 if num%9 == 0 else num%9