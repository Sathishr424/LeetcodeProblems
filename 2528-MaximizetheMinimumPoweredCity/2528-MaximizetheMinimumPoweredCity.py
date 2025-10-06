# Last updated: 7/10/2025, 3:51:47 am
class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        powers = [0] * n
        prefix = [0]
        for i in range(n):
            prefix.append(prefix[-1] + stations[i])
        
        for i in range(n):
            powers[i] += prefix[i] - prefix[max(0, i - r)]
            powers[i] += prefix[min(n, i + r + 1)] - prefix[i]

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