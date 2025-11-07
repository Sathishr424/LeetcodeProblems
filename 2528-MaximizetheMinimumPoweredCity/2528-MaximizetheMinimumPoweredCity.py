# Last updated: 7/11/2025, 2:54:27 pm
cmin = lambda x, y: x if x < y else y
cmax = lambda x, y: x if x > y else y
class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)

        prefix = [0]
        for s in stations:
            prefix.append(prefix[-1] + s)

        powers = []
        for i in range(n):
            power = prefix[i] - prefix[cmax(0, i-r)]
            power += prefix[cmin(n, i+r+1)] - prefix[i]

            powers.append(power)

        def isGood(mid):
            diff = [0] * (n + 1)
            rem = k
            curr = 0
            for i in range(n):
                curr += diff[i]
                p = curr + powers[i]
                if p < mid:
                    need = mid - p
                    if need > rem: return False
                    curr += need
                    diff[cmin(n, i + (r * 2) + 1)] -= need
                    rem -= need

            return True
        
        left = min(powers)
        right = left + k

        while left < right:
            mid = (left + right + 1) // 2

            if isGood(mid):
                left = mid
            else:
                right = mid - 1
        
        return left