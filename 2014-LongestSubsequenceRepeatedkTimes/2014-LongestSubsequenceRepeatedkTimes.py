# Last updated: 27/6/2025, 7:14:18 pm
def charToInt(char):
    return ord(char) - 97

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        n = len(s)
        freq = [0] * 26

        for char in s:
            freq[charToInt(char)] += 1

        next_index = [[-1] * 26 for _ in range(n + 1)]

        for i in range(n-1, -1, -1):
            for a in range(26):
                next_index[i][a] = next_index[i+1][a]
            next_index[i][ord(s[i]) - 97] = i

        char_limit = n // k

        candidates = [0] * 26
        for char in s:
            a = charToInt(char)
            if freq[a] >= k:
                candidates[a] = 1

        ret = ''
        used = [0] * 26
        can_use = {}

        def rec(st):
            if st in can_use: return
            can_use[st] = 1
            if len(st) == char_limit: return

            for i in range(26):
                if candidates[i] and (used[i] + 1) * k <= freq[i]:
                    used[i] += 1
                    rec(st + chr(i + 97))
                    used[i] -= 1

        rec('')

        def checkPossible(st):
            last_index = 0
            for i in range(k):
                for char in st:
                    a = charToInt(char)
                    if next_index[last_index][a] == -1: return False
                    last_index = next_index[last_index][a] + 1
            return True
            
        for st in sorted(can_use.keys(), key=lambda x: (len(x), x), reverse=True):
            if checkPossible(st):
                return st
        
        return ''