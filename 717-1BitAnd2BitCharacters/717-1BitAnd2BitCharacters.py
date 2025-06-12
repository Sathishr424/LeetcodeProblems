# Last updated: 12/6/2025, 5:47:28 am
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)
        prev = 0

        for i in range(n-1):
            if bits[i]:
                prev = not prev
            else:
                prev = 0
        
        return not prev