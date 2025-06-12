# Last updated: 12/6/2025, 5:40:13 am
class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        rem = n % 7
        return ((rem*(rem+1))//2) + (weeks * rem) + (((7*(7+1))//2) * weeks) + (((weeks*(weeks-1))//2) * 7)