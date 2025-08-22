# Last updated: 22/8/2025, 8:44:13 pm
class Solution:
    def subStrHash(self, s: str, power: int, mod: int, k: int, hashValue: int) -> str:
        n = len(s)

        def getAlp(char):
            return ord(char) - ord('a') + 1
        
        cached = pow(power, k, mod)
        
        suffix = deque([0])
        roll = 0
        for i in range(n-1, -1, -1):
            roll = roll * power % mod
            roll = (roll + getAlp(s[i])) % mod
            suffix.appendleft(roll)
    
        for i in range(n-k+1):
            right = suffix[i + k]
            left = suffix[i]
            
            diff = left - right * cached % mod
            diff %= mod
            if diff == hashValue: return s[i:i+k]
        
        return 0 