# Last updated: 12/6/2025, 5:52:31 am
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ret = [0] * 64
        mask = 0xFFFFFFFF + 1
        for num in nums:
            i = 31
            neg = False
            while num and i >= 0:
                ret[i] += num & 1 == 1
                num >>= 1
                i -= 1
        ans = 0
        i = 31
        
        for cnt in ret:
            ans += (cnt % 3) * 2**i
            i -= 1

        if ret[0] % 3: return int(ans - mask)
        return int(ans)