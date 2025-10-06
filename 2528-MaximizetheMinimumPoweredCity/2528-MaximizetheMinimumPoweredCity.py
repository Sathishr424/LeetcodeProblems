# Last updated: 6/10/2025, 11:28:01 pm
class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        powers = [0] * n
        left = 0
        power = 0
        for i in range(n):
            if i - left > r:
                power -= stations[left]
                left += 1
            power += stations[i]
            powers[i] += power

        power = 0
        right = n-1
        for i in range(n-1, -1, -1):
            if right - i > r:
                power -= stations[right]
                right -= 1
            powers[i] += power
            power += stations[i]

        def isGood(mid):
            need = [0] * n
            for i in range(n):
                need[i] = max(0, mid - powers[i])
            line = [0] * n
            curr = 0
            rem = k
            for i in range(n):
                curr += line[i]
                if need[i] > curr:
                    want = need[i] - curr
                    if want > rem: return False
                        
                    index = i + (r * 2) + 1
                    if index < n:
                        line[index] -= want
                    
                    rem -= want
                    curr += want
            return True

        left = min(powers)
        right = max(powers) + k

        while left < right:
            mid = (left + right + 1) // 2

            if isGood(mid):
                left = mid
            else:
                right = mid - 1

        return left