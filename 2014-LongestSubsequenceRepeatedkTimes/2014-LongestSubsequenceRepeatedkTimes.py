# Last updated: 27/6/2025, 10:14:24 pm
def charToInt(char):
    return ord(char) - 97
cmax = lambda x, y: x if x > y else y

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        n = len(s)
        alps = [charToInt(char) for char in s]
        freq = [[0] * 26 for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(26):
                freq[i][j] = freq[i-1][j]

            freq[i][alps[i - 1]] += 1

        stack = [(0, n-1)]
        ret = 0
        
        while stack:
            l, r = stack.pop()
            if r - l + 1 <= ret or r -l + 1 < k: continue
            possible = True
            for i in range(l, r+1):
                if freq[r+1][alps[i]] - freq[l][alps[i]] < k:
                    stack.append((l, i-1))
                    stack.append((i+1, r))
                    possible = False
                    break
            if possible:
                ret = max(ret, r - l + 1) 
        
        return ret