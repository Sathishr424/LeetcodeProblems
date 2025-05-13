# Last updated: 13/5/2025, 12:09:28 pm
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = 10**9 + 7
        # ab
        # 26, 25
        # adefg
        #   fgh

        freq = [0] * 26

        for char in s:
            freq[ord(char) - 97] += 1
        # print(freq)
        for i in range(t):
            curr = freq[25]
            for num in range(24, -1, -1):
                if freq[num]:
                    freq[num+1] = (freq[num+1] + freq[num]) % mod
                    freq[num] = 0
            
            if freq[25]:
                freq[0] = (freq[0] + curr) % mod
                freq[1] = (freq[1] + curr) % mod
                freq[25] -= curr
            # print(t+1, freq, sum(freq))
        
        return sum(freq) % mod
                