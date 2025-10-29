# Last updated: 29/10/2025, 3:04:09 pm
class Solution:
    def smallestNumber(self, n: int) -> int:
        return (1 << n.bit_length()) - 1