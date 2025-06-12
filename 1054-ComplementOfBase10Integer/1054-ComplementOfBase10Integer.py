# Last updated: 12/6/2025, 5:44:25 am
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0: return 1
        ans = 0
        index = 0
        while n:
            ans += (2**index) * ((n+1) % 2)
            n //= 2
            index += 1
        return ans