# Last updated: 12/6/2025, 5:49:32 am
class Solution:
    def countSegments(self, s: str) -> int:
        ans = 0
        prev = ' '

        for w in s:
            if w != ' ' and prev == ' ': ans += 1
            prev = w
        
        return ans
