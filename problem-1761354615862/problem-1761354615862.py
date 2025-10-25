# Last updated: 25/10/2025, 6:40:15 am
week_sum = 7 * 8 // 2

class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        rem = n % 7

        total = 0
        total += week_sum * weeks
        total += (weeks * (weeks - 1)) // 2 * 7

        total += rem * (rem + 1) // 2 + (weeks * rem)

        return total

            