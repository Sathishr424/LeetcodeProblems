# Last updated: 23/4/2025, 9:59:40 pm
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        # prefixCnt - ((maxi - currElement) * cnt)

        ret = 1
        maxi = nums[-1] + 1
        prefix = [0]
        for i in range(n):
            prefix.append(prefix[-1] + (maxi - nums[i]))
        
        def bn_l(l, r, index, val, rem):
            while l < r:
                mid = (l + r) // 2
                
                diff = index - mid
                s = prefix[index] - prefix[mid]
                s = s - (val * diff)

                if s <= rem:
                    r = mid
                else:
                    l = mid + 1
            
            return l
        
        def bn_r(l, r, index, val, rem):
            while l < r:
                mid = (l + r) // 2

                diff = index - mid
                s = prefix[mid+1] - prefix[index]
                s = s - (val * diff)

                if s >= rem:
                    r = mid
                else:
                    l = mid + 1
            
            return l

        for i in range(1, n):
            num = nums[i]

            left = bn_l(0, i, i, maxi-num, k)
            s = abs(prefix[i] - prefix[left])
            right = bn_r(i, n-1, i, maxi-num, k-s)

            ret = max(ret, right-left+1)
        
        return ret