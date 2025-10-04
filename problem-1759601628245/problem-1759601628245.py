# Last updated: 4/10/2025, 11:43:48 pm
N = 10**5 + 1
fact = [1] * N
mod = 10**9 + 7

for i in range(1, N):
    fact[i] = fact[i - 1] * i % mod

inv_fact = [1] * N
inv_fact[N-1] = pow(fact[N-1], mod - 2, mod)

for i in range(N-2, -1, -1):
    inv_fact[i] = inv_fact[i + 1] * (i + 1) % mod

class Solution:
    def countAnagrams(self, s: str) -> int:
        # too => too, oto, oot
        # hot => hot, hto, oht, oth, tho, toh

        ans = 1
        words = s.split(' ')
        for word in words:
            freq = defaultdict(int)
            for char in word:
                freq[char] += 1

            f = fact[len(word)]
            for char in freq:
                f = f * inv_fact[freq[char]] % mod
            ans = ans * f % mod
        
        return ans