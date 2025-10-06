# Last updated: 6/10/2025, 9:50:14 pm
class Solution:
    def minimumPartition(self, st: str, k: int) -> int:
        nums = [int(d) for d in st]
        n = len(nums)
        nums_k = [int(d) for d in str(k)]
        m = len(nums_k)
        if max(nums) > k: return -1

        @cache
        def helper(index):
            if nums[index] > nums_k[0]:
                return rec(index + 1, False, True, 1) + 1
            elif nums[index] < nums_k[0]:
                return rec(index + 1, False, False, 1) + 1
            else:
                return rec(index + 1, True, False, 1) + 1
        
        # 554
        @cache
        def rec(index, strict, is_large, pos):
            if index == n:
                return 0

            if (is_large and pos == m-1) or pos == m:
                return helper(index)
            
            ans = helper(index)
            if strict:
                if nums[index] <= nums_k[pos]:
                    ans = min(ans, rec(index + 1, nums[index] == nums_k[pos], False, pos + 1))
                elif pos < m-1:
                    ans = min(ans, rec(index + 1, False, True, pos + 1))
            else:
                ans = min(ans, rec(index + 1, False, is_large, pos + 1))
            
            return ans

        ans = helper(0)
        rec.cache_clear()
        helper.cache_clear()
        return ans