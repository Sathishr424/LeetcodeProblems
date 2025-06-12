# Last updated: 12/6/2025, 5:38:32 am
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        cnt = 0
        while num1 != 0 and num2 != 0:
            if num1 > num2:
                num1 -= num2
            else:
                num2 -= num1
            cnt += 1
        return cnt