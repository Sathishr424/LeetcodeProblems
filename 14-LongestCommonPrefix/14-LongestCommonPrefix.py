# Last updated: 12/6/2025, 5:55:19 am
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = 201
        for i in range(len(strs)):
            n = min(n, len(strs[i]))
        ans = 0
        for i in range(n):
            prev = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != prev: return strs[0][:ans]
            ans = i+1
        return strs[0][:ans]