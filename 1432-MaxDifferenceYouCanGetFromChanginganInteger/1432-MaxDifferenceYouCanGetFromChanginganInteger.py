# Last updated: 15/6/2025, 8:09:28 am
class Solution:
    def maxDiff(self, num: int) -> int:
        digit = -1
        def getMaxi(num):
            nonlocal digit
            if num == 0: return 0

            new_num = getMaxi(num // 10)
            rem = num % 10
            if digit == -1:
                if rem != 9:
                    digit = rem
            
            if rem == digit:
                return new_num * 10 + 9
            return new_num * 10 + rem
        
        replace = 1

        def getMini(num):
            nonlocal digit, replace
            if num == 0: return 0

            new_num = getMini(num // 10)
            rem = num % 10
            if digit == -1:
                if new_num == 0:
                    if rem > 1: digit = rem
                elif rem > 1:
                    digit = rem
                    replace = 0
            
            if rem == digit:
                return new_num * 10 + replace
            return new_num * 10 + rem
            
        
        maxi = getMaxi(num)
        digit = -1
        mini = getMini(num)
        # print(maxi, mini)
        return maxi - mini