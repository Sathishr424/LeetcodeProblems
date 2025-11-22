# Last updated: 22/11/2025, 8:02:27 pm
class Solution:
    def minimumFlips(self, n: int) -> int:
        st = bin(n)[2:]
        rev = st[::-1]

        cnt = 0
        for i in range(len(st)):
            if st[i] != rev[i]:
                cnt += 1

        return cnt