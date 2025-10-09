# Last updated: 10/10/2025, 2:20:05 am
class Solution:
    def isReachable(self, targetX: int, targetY: int) -> bool:
        def isPowerOf2(num):
            return num & (num - 1) == 0
        
        return isPowerOf2(targetX) or isPowerOf2(targetY) or isPowerOf2(gcd(targetX, targetY))