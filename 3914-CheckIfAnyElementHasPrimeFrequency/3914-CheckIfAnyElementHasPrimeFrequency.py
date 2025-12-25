# Last updated: 12/25/2025, 7:10:49 PM
is_prime = [1] * 101
is_prime[0] = 0
is_prime[1] = 0
for i in range(2, int(101 ** 0.5) + 1):
    if is_prime[i] == 0: continue

    for j in range(i*i, 101, i):
        is_prime[j] = 0

class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        for key in freq:
            if is_prime[freq[key]]: return True

        return False