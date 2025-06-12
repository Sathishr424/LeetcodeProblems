# Last updated: 12/6/2025, 5:46:03 am
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        match_s = []
        match_t = []
        for c in s:
            if c == '#':
                if match_s: match_s.pop()
            else:
                match_s.append(c)
        for c in t:
            if c == '#':
                if match_t: match_t.pop()
            else:
                match_t.append(c)
        
        return ''.join(match_s) == ''.join(match_t)
        