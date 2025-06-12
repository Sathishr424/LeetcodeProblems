# Last updated: 12/6/2025, 5:34:59 am
class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        prev = ''
        cnt = 0
        for char in s:
            if char == prev:
                cnt += 1
            else:
                if cnt == k: return True
                cnt = 1
                prev = char
    
        return cnt == k
                