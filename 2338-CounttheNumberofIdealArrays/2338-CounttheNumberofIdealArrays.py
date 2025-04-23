# Last updated: 23/4/2025, 10:30:49 pm
cmax = lambda x, y: x if x > y else y
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        # prefixCnt - ((maxi - currElement) * cnt)

        ret = 1
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        
        def bn_l(l, r, index):
            while l < r:
                mid = (l + r) // 2

                diff = index - mid
                s = prefix[index] - prefix[mid]
                s = abs((nums[index] * diff) - s)

                if s <= k:
                    r = mid
                else:
                    l = mid + 1
            
            return l

        for i in range(len(nums)):
            left = bn_l(0, i, i)
            ret = cmax(ret, i-left+1)
        
        return ret