# Last updated: 12/25/2025, 7:08:51 PM
class Solution:
    def minimumTime(self, d: List[int], r: List[int]) -> int:
        tot = sum(d)
        def isGood(target):
            possible = target // r[0]
            possible += target // r[1]

            possible -= target // lcm(r[0], r[1])

            common = target - possible

            lf = target - (target // r[0])
            ri = target - (target // r[1])

            return lf >= d[0] and ri >= d[1] and (lf + ri) - common >= tot

        left = max(d)
        right = 10**10

        while left < right:
            mid = (left + right) // 2

            if isGood(mid):
                right = mid
            else:
                left = mid + 1
        
        return left