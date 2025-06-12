# Last updated: 12/6/2025, 5:55:30 am
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x <= 9: return x >= 0
        
        y = 0
        dig = 1
        tmp = x
        while x:
            rem = x % 10
            x //= 10
            y = (y*10) + rem
        return y == tmp