# Last updated: 14/6/2025, 11:29:51 am
class Solution:
    def minMaxDifference(self, num: int) -> int:
        digit = -1
        def rec(num, replace):
            nonlocal digit
            if num == 0: return 0

            new_num = rec(num // 10, replace)
            rem = num % 10

            if digit == -1 and rem != replace:
                digit = rem
            
            if rem == digit:
                return new_num * 10 + replace
            return new_num * 10 + rem
        
        maxi = rec(num, 9)
        digit = -1
        mini = rec(num, 0)

        return maxi - mini