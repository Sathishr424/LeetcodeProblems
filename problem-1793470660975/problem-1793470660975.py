# Last updated: 10/31/2026, 11:47:40 PM
1class Solution:
2    def minPenalty(self, period: int, lights: list[int], arrivalTime: list[int]) -> int:
3        m = len(arrivalTime)
4
5        rs = [t % period for t in arrivalTime]
6        max_l = max(lights)
7
8        rs.sort(reverse=True)
9
10        best = 0
11        i = 0
12        while i < m and rs[i] >= max_l:
13            best = max(best, period - rs[i])
14            i += 1
15        return best