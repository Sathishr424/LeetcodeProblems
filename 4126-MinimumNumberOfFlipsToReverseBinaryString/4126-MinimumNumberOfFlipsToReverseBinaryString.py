# Last updated: 12/25/2025, 7:08:04 PM
class Solution:
    def minimumFlips(self, n: int) -> int:
        st = bin(n)[2:]
        rev = st[::-1]

        cnt = 0
        for i in range(len(st)):
            if st[i] != rev[i]:
                cnt += 1

        return cnt