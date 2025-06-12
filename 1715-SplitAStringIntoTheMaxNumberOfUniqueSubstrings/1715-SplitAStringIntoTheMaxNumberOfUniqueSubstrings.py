# Last updated: 12/6/2025, 5:40:50 am
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        added = {}
        def rec(index, st):
            nonlocal added
            ans = 0
            if st not in added:
                if index == len(s): return len(added) + 1

                added[st] = 1
                ans = rec(index+1, s[index])
                del added[st]
            
            elif index == len(s): return 0

            return max(ans, rec(index+1, st + s[index]))

        return rec(1, s[0])