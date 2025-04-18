# Last updated: 18/4/2025, 6:46:31 am
class Solution:
    def countAndSay(self, n: int) -> str:
        st = '1'
        i = 1
        while i < n:
            prev = st[0]
            cnt = 1
            new_st = ''
            for char in st[1:]:
                if char == prev:
                    cnt += 1
                else:
                    new_st += f"{cnt}{prev}"
                    cnt = 1
                prev = char
            new_st += f"{cnt}{prev}"
            st = new_st
            i += 1
        
        return st