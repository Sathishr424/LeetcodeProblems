# Last updated: 12/25/2025, 7:09:28 PM
class Solution:
    def maxXorSubsequences(self, nums: List[int]) -> int:
        basis = [0] * 32
        basis_used = [0] * 32

        for num in nums:
            while num:
                msb = num.bit_length() - 1
                if basis_used[msb] == 0:
                    basis[msb] = num
                    basis_used[msb] = 1
                    break
                else:
                    num = basis[msb] ^ num
        
        ans = 0
        for i in range(31, -1, -1):
            ans = max(ans, ans ^ basis[i])
        
        return ans
