# Last updated: 12/6/2025, 5:46:34 am
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        tmp = ""
        for w in s:
            tmp += w
        for w in s:
            tmp += w
        
        n = len(s)

        for i in range(n, len(tmp)):
            if tmp[i-n:i] == goal: return True
        return False