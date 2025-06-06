# Last updated: 6/6/2025, 1:19:44 pm
class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)
        ret = ''
        t = []
        index = 0
        
        freq = [0] * 26

        for i in range(n):
            a = ord(s[i]) - 97
            freq[a] += 1
        
        def addItToT(to_find):
            nonlocal index, ret
            for i in range(index, n):
                a = ord(s[i]) - 97
                freq[a] -= 1
                if a == to_find:
                    ret += s[i]
                    index = i + 1
                    break
                t.append(s[i])
        
        while index < n:
            i = 0
            while i < 26 and freq[i] == 0: 
                i += 1

            if not t or ord(t[-1]) - 97 > i:
                addItToT(i)
            else:
                ret += t.pop()
        
        return ret + ''.join(t[::-1])



            
