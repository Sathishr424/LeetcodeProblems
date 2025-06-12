# Last updated: 12/6/2025, 5:40:40 am
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        left = {}
        ans = -1
        for i in range(len(s)):
            if s[i] not in left:
                left[s[i]] = i
            else:
                ans = max(ans, i-left[s[i]]-1)
        return ans