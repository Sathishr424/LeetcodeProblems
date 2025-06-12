# Last updated: 12/6/2025, 5:54:15 am
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans = int(s[-1] != ' ')

        for i in range(len(s)-2, -1, -1):
            if s[i] == ' ': 
                if s[i+1] != ' ': return ans
            else: ans += 1

        return ans