# Last updated: 6/6/2025, 12:42:28 pm
class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)
        ret = ''
        t = []
        index = 0
        
        cnts = [0] * 26
        start = [deque([]) for _ in range(26)]

        smalli = 0
        for i in range(n):
            if s[i] < s[smalli]:
                smalli = i
            a = ord(s[i]) - 97
            cnts[a] += 1
            start[a].append(i)
        
        def addItToT(index_):
            nonlocal index, ret
            for i in range(index, index_):
                t.append(s[i])
                a = ord(s[i]) - 97
                cnts[a] -= 1
                start[a].popleft()
            
            a = ord(s[index_]) - 97
            start[a].popleft()
            cnts[a] -= 1

            ret += s[index_]
            index = index_+1
        
        addItToT(smalli)

        while index < n:
            # print('index:', index)
            # print('cnts:', cnts)
            # print('start:', start)
            # print('T:', t)
            # print('ret:', ret)
            # print()
            for i in range(26):
                if not t:
                    if cnts[i] and start[i][0] >= index:
                        addItToT(start[i][0])
                        break
                elif t:
                    a = ord(t[-1]) - 97
                    if a <= i:
                        ret += t.pop()
                        break
                    elif cnts[i] and start[i][0] >= index:
                        addItToT(start[i][0])
                        break
        
        while t:
            ret += t.pop()
        
        return ret