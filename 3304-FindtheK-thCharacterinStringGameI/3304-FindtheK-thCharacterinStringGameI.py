# Last updated: 3/7/2025, 5:43:36 am
class Solution:
    def kthCharacter(self, k: int) -> str:
        # a, ab, abbc, abbcbccd
        st = 'a'
        while len(st) < k:
            new_st = st
            for char in st:
                a = ord(char) - ord('a')
                new_st += chr((a + 1) % 26 + ord('a'))
            st = new_st
        
        return st[k-1]