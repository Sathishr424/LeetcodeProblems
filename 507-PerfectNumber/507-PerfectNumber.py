# Last updated: 12/6/2025, 5:48:45 am
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 0: return False

        total = 0
        i = 1

        while i * i <= num:
            if num % i == 0:
                total += i
                if i * i != num: total += num / i
            i += 1
        
        return total - num == num