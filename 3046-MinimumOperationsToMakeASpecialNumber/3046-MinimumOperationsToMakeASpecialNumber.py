# Last updated: 12/6/2025, 5:36:21 am
class Solution:
    def minimumOperations(self, num: str) -> int:
        n = len(num)
        # 00 75 50 25
        zero = n
        five = n

        for i in range(n-1, -1, -1):
            if (num[i] == '5' or num[i] == '0') and zero != n: return (zero-i-1)+(n-zero-1)
            elif (num[i] == '2' or num[i] == '7') and five != n: return (five-i-1)+(n-five-1)

            if num[i] == '5':
                five = min(five, i)
            if num[i] == '0':
                zero = min(zero, i)
        
        return n if zero == n else zero+(n-zero-1)
