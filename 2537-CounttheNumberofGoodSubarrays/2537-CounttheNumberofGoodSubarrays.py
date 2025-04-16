# Last updated: 16/4/2025, 3:15:45 pm
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pairs = defaultdict(int)
        total = 0

        left = 0
        ret = 0
        good = 0

        for i in range(n):
            pairs[nums[i]] += 1
            total += pairs[nums[i]]-1

            while total >= k:
                ret += left+(n-i)-good
                good += 1

                num = nums[left]
                pairs[num] -= 1
                total -= pairs[num]

                left += 1
            
        return ret