# Last updated: 12/6/2025, 5:47:04 am
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = set([2,3,5,7.,11,13,17,19,23])
        ans = 0

        for i in range(left, right+1):
            num = i
            cnt = 0
            while num:
                cnt += num % 2
                num //= 2
            ans += cnt in primes
        return ans