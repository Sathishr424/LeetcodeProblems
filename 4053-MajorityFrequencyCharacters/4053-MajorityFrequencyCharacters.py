# Last updated: 12/25/2025, 7:08:46 PM
class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        n = len(s)

        freq = defaultdict(int)

        max_freq = 0
        for char in s:
            freq[char] += 1
            max_freq = max(max_freq, freq[char])

        best = s[0]
        for k in range(max_freq + 1, 0, -1):
            st = ''
            for char in freq:
                if freq[char] == k:
                    st += char

            if len(st) > len(best):
                best = st

        return best
            

        