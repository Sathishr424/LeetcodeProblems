# Last updated: 13/5/2025, 12:33:22 pm
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = 10**9 + 7
        freq = [0] * 26

        for char in s:
            freq[ord(char) - 97] += 1

        for i in range(t):
            z = freq[25]
            freq[25] = 0
            for num in range(24, -1, -1):
                freq[num+1] = freq[num]
                freq[num] = 0
            
            freq[0] = freq[0] + z
            freq[1] = freq[1] + z
        
        return sum(freq) % mod
                