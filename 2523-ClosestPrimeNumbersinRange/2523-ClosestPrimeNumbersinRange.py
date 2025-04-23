# Last updated: 23/4/2025, 7:53:24 am
N = 10**6

is_prime = [True] * (N+1)
is_prime[0] = False
is_prime[1] = False

for i in range(2, int(N**0.5) + 1):
    if not is_prime[i]: continue
    for j in range(i*i, N+1, i):
        is_prime[j] = False

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        prev = -1
        ret = [-1, -1]
        mini = float('inf')
        for i in range(left, right+1):
            if is_prime[i]:
                if prev != -1 and i - prev < mini:
                    if prev-i == 2: return [prev, i]
                    ret = [prev, i]
                    mini = i-prev
                prev = i
        
        return ret

