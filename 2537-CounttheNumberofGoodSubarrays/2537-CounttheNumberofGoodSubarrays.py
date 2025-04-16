# Last updated: 16/4/2025, 3:17:09 pm
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pairs = defaultdict(int)

        total = 0
        left = 0
        ret = 0

        for i in range(n):
            pairs[nums[i]] += 1
            total += pairs[nums[i]]-1

            while total >= k:
                ret += n-i

                pairs[nums[left]] -= 1
                total -= pairs[nums[left]]

                left += 1
            
        return ret