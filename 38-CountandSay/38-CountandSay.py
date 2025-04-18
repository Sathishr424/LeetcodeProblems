# Last updated: 18/4/2025, 6:48:11 am
class Solution:
    def countAndSay(self, n: int) -> str:
        st = '1'
        i = 1
        while i < n:
            prev = st[0]
            cnt = 1
            new_st = ''
            for j in range(1, len(st)):
                if st[j] == prev:
                    cnt += 1
                else:
                    new_st += f"{cnt}{prev}"
                    cnt = 1
                prev = st[j]
            new_st += f"{cnt}{prev}"
            st = new_st
            i += 1
        
        return st