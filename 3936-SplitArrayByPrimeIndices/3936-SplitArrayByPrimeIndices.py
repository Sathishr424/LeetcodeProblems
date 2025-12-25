# Last updated: 12/25/2025, 7:10:35 PM
N = 10 ** 5 + 1
is_prime = [True] * N

is_prime[0] = False
is_prime[1] = False

for i in range(2, int(N ** 0.5) + 1):
    if not is_prime[i]: continue
    for j in range(i * i, N, i):
        is_prime[j] = False

class Solution:
    def splitArray(self, nums: List[int]) -> int:
        n = len(nums)

        a = 0
        b = 0

        for i in range(n):
            if is_prime[i]:
                a += nums[i]
            else:
                b += nums[i]

        return abs(a - b)