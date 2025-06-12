# Last updated: 12/6/2025, 5:45:35 am
class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        alice = sum(aliceSizes)
        bob = 0
        hash = {}
        for b in bobSizes:
            bob += b
            hash[b] = 1

        for candy in aliceSizes:
            val = ((bob+candy) - (alice-candy)) / 2
            if val in hash:
                return [candy, int(val)]