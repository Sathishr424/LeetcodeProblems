# Last updated: 4/4/2025, 12:29:50 am
class Solution:
    def maxDifference(self, s: str) -> int:
        count = defaultdict(int)

        for char in s:
            count[char] += 1
        
        odd = 0
        even = float('inf')

        for char in count:
            if count[char] % 2 == 0:
                even = min(even, count[char])
            else:
                odd = max(odd, count[char])

        return odd - even