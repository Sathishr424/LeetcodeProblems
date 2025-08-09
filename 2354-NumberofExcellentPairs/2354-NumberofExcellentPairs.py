# Last updated: 10/8/2025, 4:59:23 am
class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        ret = 0
        uniq = set(nums)

        bits = []
        for num in uniq:
            bits.append(num.bit_count())
        
        bits.sort()
        n = len(bits)

        for i in range(n):
            need = max(0, k - bits[i])

            index = bisect_left(bits, need)

            ret += n - index
        
        return ret