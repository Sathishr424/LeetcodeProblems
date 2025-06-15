# Last updated: 15/6/2025, 8:12:20 am
class Solution:
    def maxDiff(self, num: int) -> int:
        digit = -1
        find = 9
        replace = 9
        
        def rec(num):
            nonlocal digit, replace
            if num == 0: return 0

            new_num = rec(num // 10)
            rem = num % 10

            if digit == -1:
                if new_num == 0:
                    if rem != find:
                        digit = rem
                else:
                    if find == 1:
                        if rem > 1:
                            digit = rem
                            replace = 0
                    elif rem != find:
                        digit = rem
            
            if rem == digit:
                return new_num * 10 + replace
            
            return new_num * 10 + rem
        
        maxi = rec(num)
        digit = -1
        find = 1
        replace = 1
        mini = rec(num)
        return maxi - mini