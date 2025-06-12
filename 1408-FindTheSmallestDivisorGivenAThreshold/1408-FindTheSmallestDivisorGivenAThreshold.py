# Last updated: 12/6/2025, 5:42:33 am
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l = 1
        r = max(nums)

        ret = r

        while l <= r:
            mid = (l+r) // 2
            # print(l, mid, r)

            tot = 0
            for num in nums:
                tot += ceil(num/mid)
                if tot > threshold: break
            # print(tot)
            if tot <= threshold:
                ret = mid
                r = mid-1
            else:
                l = mid+1
        
        return ret
