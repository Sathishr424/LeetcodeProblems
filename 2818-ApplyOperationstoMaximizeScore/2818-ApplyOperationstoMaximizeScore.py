# Last updated: 12/5/2025, 4:37:33 pm
N = 10**5 + 1
is_prime = [True] * N
is_prime[0] = False
for i in range(2, int(N ** 0.5) + 1):
    if not is_prime[i]: continue

    for num in range(i*i, N, i):
        is_prime[num] = False

primes = []
for num in range(2, N):
    if is_prime[num]: primes.append(num)

def getPrimeScore(num):
    if num == 1: return 0
    elif is_prime[num]: return 1

    score = 0
    for x in primes:
        if num % x: continue
        while num % x == 0:
            num //= x
        score += 1
        if num == 1: return score
        elif is_prime[num]: return score + 1

mod = 10**9 + 7

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ret = 1

        scores = [getPrimeScore(num) for num in nums]
        arr = []

        for i, num in enumerate(nums):
            arr.append((num, i))
        
        arr.sort(reverse=True)

        left = [-1] * n
        right = [n] * n
        stack = []

        for i in range(n-1, -1, -1):
            score = scores[i]
            while stack and stack[-1][1] <= score:
                left[stack.pop()[0]] = i
            
            stack.append((i, score))
        
        stack = []
        for i in range(n):
            score = scores[i]
            while stack and stack[-1][1] < score:
                right[stack.pop()[0]] = i
            
            stack.append((i, score))

        for num, i in arr:
            l = i - left[i]
            r = right[i] - i
            possible = min(k, l * r)

            ret = ret * pow(num, possible, mod) % mod
            k -= possible
            if k == 0: break

        return ret