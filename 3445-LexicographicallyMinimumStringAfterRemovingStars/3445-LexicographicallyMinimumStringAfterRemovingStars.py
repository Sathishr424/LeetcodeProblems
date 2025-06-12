# Last updated: 12/6/2025, 5:35:38 am
class Solution:
    def clearStars(self, s: str) -> str:
        n = len(s)

        deleted = [0] * n
        freq = [[] for _ in range(26)]
        for i in range(n):
            if s[i] == '*':
                deleted[i] = 1
                for i in range(26):
                    if freq[i]:
                        deleted[freq[i].pop()] = 1
                        break
            else:
                freq[ord(s[i]) - 97].append(i)
        
        return ''.join([s[i] for i in range(n) if deleted[i] == 0])
                
