# Last updated: 12/6/2025, 5:53:27 am
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        ret = []
        def rec(index, st, sep):
            if index == n:
                if sep == 4: ret.append(st[:-1])
                return
            elif sep >= 4: return
            prev = 0
            if s[index] == '0':
                return rec(index+1, st+'0.', sep+1)
            for i in range(index, n):
                prev = (prev * 10) + int(s[i])
                if prev > 255: return
                rec(i+1, st+str(prev)+'.', sep+1)
        
        rec(0, "", 0)
        return ret