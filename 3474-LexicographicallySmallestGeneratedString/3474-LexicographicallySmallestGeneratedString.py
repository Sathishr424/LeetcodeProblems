# Last updated: 5/6/2025, 9:29:33 pm
def getLPS(s):
    n = len(s)
    lps = [0] * n
    
    i = 1
    j = 0

    while i < n:
        if s[i] == s[j]:
            j += 1
            lps[i] = j
        elif j > 0:
            j = lps[j-1]
            continue
        i += 1
    return lps

class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)

        Ts = []
        Fs = []

        for i in range(n):
            if str1[i] == 'T':
                Ts.append(i)
            else:
                Fs.append(i)
        
        lps = getLPS(str2)
        # print(lps)

        def check(indexes):
            for i in range(len(indexes)-1):
                index = indexes[i]
                next = min(index+m, indexes[i+1])
                diff = next-index
                if m-diff > 0 and lps[-1] != m-diff: 
                    # print(index, next, (diff, m-diff))
                    return False
            return True
        
        if not check(Ts): return ''
        
        ret = ['-'] * (m+n-1)

        i = 0
        for i, index in enumerate(Ts):
            next = index+m
            if i+1 < len(Ts):
                next = min(next, Ts[i+1])

            for j in range(index, next):
                ret[j] = str2[j-index]
        
        tmp = ''.join(ret)
        for index in Fs:
            if tmp[index:index+m] == str2: return ''
        
        for i in range(n):
            if ret[i] == '-':
                ret[i] = 'a'
                tmp = ''.join(ret)
                for j in range(max(0, i-m+1), i+1):
                    if str1[j] == 'F' and tmp[j:j+m] == str2:
                        ret[i] = 'b'
                        break
        
        for i in range(n, len(ret)):
            if ret[i] == '-':
                ret[i] = 'a'
        
        ans = ''.join(ret)
        if str1[-1] == 'F' and ans[-m:] == str2:
            return ans[:-1] + 'b'

        return ans
