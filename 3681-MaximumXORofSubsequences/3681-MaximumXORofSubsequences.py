# Last updated: 23/9/2025, 3:32:35 pm
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
