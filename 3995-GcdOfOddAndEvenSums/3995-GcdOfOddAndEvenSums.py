# Last updated: 12/25/2025, 7:09:25 PM
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        even = 0
        rem = n
        num = 2
        while rem:
            even += num
            num += 2
            rem -= 1

        odd = 0
        rem = n
        num = 1
        while rem:
            odd += num
            num += 2
            rem -= 1
        
        # print(even, odd)
        return gcd(even, odd)