# Last updated: 7/11/2025, 2:44:39 pm
class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)

        prefix = [0]
        for s in stations:
            prefix.append(prefix[-1] + s)

        powers = []
        for i in range(n):
            power = prefix[i] - prefix[max(0, i-r)]
            power += prefix[min(n, i+r+1)] - prefix[i]

            powers.append(power)

        def isGood(mid):
            stack = deque([])
            rem = k
            extra = 0
            for i in range(n):
                while stack and abs(i - stack[0][0]) > r: 
                    extra -= stack.popleft()[1]
                curr = powers[i] + extra
                if curr < mid:
                    need = mid - curr
                    if need > rem: return False
                    stack.append((min(n, i + r), need))
                    rem -= need
                    extra += need

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