# Last updated: 15/7/2025, 10:36:23 am
class Solution:
    def minAnagramLength(self, s: str) -> int:
        n = len(s)

        uniq = defaultdict(int)
        for char in s:
            uniq[char] += 1
        uniq_len = len(uniq)

        for window in range(1, n // 2 + 1):
            if n % window != 0 or window < uniq_len: continue
            freq = [0] * 26
            for i in range(window):
                freq[ord(s[i]) - 97] += 1

            match = True
            for i in range(0, n, window):
                duplicate = freq[:]
                need = uniq_len
                for j in range(i, i + window):
                    duplicate[ord(s[j]) - 97] -= 1
                    if duplicate[ord(s[j]) - 97] == 0:
                        need -= 1
                # print(window, need, (i, s[i:i+window]))
                if need != 0: 
                    match = False
                    break
            
            if match: return window
        
        return n