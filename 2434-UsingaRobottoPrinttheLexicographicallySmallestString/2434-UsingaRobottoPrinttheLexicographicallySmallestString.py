# Last updated: 6/6/2025, 1:08:54 pm
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
            # print('index:', index)
            # print('freq:', freq)
            # print('T:', t)
            # print('ret:', ret)
            # print()
            for i in range(26):
                if not t:
                    if freq[i]: 
                        addItToT(i)
                        break
                else:
                    if ord(t[-1]) - 97 <= i:
                        ret += t.pop()
                        break
                    elif freq[i]:
                        addItToT(i)
                        break
        
        while t: ret += t.pop()
        return ret



            
