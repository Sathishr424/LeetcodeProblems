# Last updated: 23/11/2025, 8:34:41 am
class Solution:
    def maxBalancedSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        def findAns(nums):
            ans = 0
            hash = defaultdict(dict)
            hash[0][0] = -1
            even = 0
            odd = 0
            xor = 0
            for i in range(n):
                if nums[i] % 2 == 0:
                    even += 1
                else:
                    odd += 1
                xor ^= nums[i]
                diff = even - odd
                if diff in hash and xor in hash[diff]:
                    ans = max(ans, i - hash[diff][xor])
                if xor not in hash[diff]:
                    hash[diff][xor] = i

                # print(i, nums, diff, xor, dict(hash))
            
            return ans
        
        return findAns(nums)