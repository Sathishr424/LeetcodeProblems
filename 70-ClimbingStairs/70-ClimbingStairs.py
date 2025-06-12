# Last updated: 12/6/2025, 5:54:00 am
class Solution:
    def climbStairs(self, n: int) -> int:
        first = 1
        second = 1

        for i in range(n-1):
            tmp = second
            second = second + first
            first = tmp
 
        return second