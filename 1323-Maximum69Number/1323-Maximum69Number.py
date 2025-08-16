# Last updated: 16/8/2025, 8:58:20 am
class Solution:
    def maximum69Number (self, num: int) -> int:
        def rec(num):
            if num == 0: return 0
            prev = rec(num // 10)
            if prev == num // 10:
                if num % 10 == 6:
                    return num // 10 * 10 + 9
                return num
            else:
                return prev * 10 + (num % 10)
        
        return rec(num)