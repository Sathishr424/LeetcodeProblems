# Last updated: 12/25/2025, 7:10:57 PM
class Solution:
    def partitionString(self, s: str) -> List[str]:
        n = len(s)
        ret = []
        curr = ''
        there = {}
        for char in s:
            curr += char
            if curr not in there:
                ret.append(curr)
                there[curr] = 1
                curr = ''

        return ret