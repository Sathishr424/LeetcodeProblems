# Last updated: 23/4/2025, 10:27:16 pm
cmax = lambda x, y: x if x > y else y
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        # prefixCnt - ((maxi - currElement) * cnt)

        ret = 1
        prefix = [0]
        for i in range(n):
            prefix.append(prefix[-1] + nums[i])
        
        def bn_l(l, r, index, num, rem):
            while l < r:
                mid = (l + r) // 2

                diff = index - mid
                s = prefix[index] - prefix[mid]
                s = abs((num * diff) - s)

                if s <= rem:
                    r = mid
                else:
                    l = mid + 1
            
            return l
        
        def bn_r(l, r, index, num, rem):
            while l < r:
                mid = (l + r) // 2

                diff = index - mid
                s = prefix[mid+1] - prefix[index]
                s = abs((num * diff) - s)

                if s > rem:
                    r = mid
                else:
                    l = mid + 1
            
            return l

        for i in range(1, n):
            num = nums[i]

            left = bn_l(0, i, i, num, k)
            s = abs(prefix[i] - prefix[left])
            right = bn_r(i+1, n, i, num, k-s)
            ret = cmax(ret, right-left)
        
        return ret