# Last updated: 12/6/2025, 5:43:01 am
class Solution:
    def makeFancyString(self, s: str) -> str:
        ret = ""
        prev = None
        cnt = 0
        for char in s:
            if char == prev:
                if cnt == 2: continue
                cnt += 1
            else:
                prev = char
                cnt = 1
            ret += char
        return ret