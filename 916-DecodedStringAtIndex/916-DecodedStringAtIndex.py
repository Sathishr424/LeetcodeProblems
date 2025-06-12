# Last updated: 12/6/2025, 5:45:44 am
class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        cnt = 0
        for i in range(len(s)):
            c = s[i]
            if c.isdigit():
                cnt *= int(c)
            else:
                cnt += 1
            if cnt >= k: break
        
        for j in range(i, -1, -1):
            c = s[j]
            if c.isdigit():
                cnt = cnt // int(c)
                k = k % cnt
            else:
                if k == 0 or k == cnt: return c
                cnt -= 1
        return ""