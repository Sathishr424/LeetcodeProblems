# Last updated: 10/14/2026, 2:54:46 PM
1class Solution:
2    def maxSumOfSquares(self, num: int, sum: int) -> str:
3        rem = num
4        rem_sum = sum
5
6        ret = ""
7        while rem and rem_sum:
8            can = min(9, rem_sum)
9            rem_sum -= can
10            ret += str(can)
11            rem -= 1
12
13        return ret + '0' * rem if rem_sum == 0 else ""