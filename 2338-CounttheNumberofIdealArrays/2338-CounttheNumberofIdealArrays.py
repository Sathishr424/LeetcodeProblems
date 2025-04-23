# Last updated: 23/4/2025, 9:54:55 pm
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)

        nums.sort()

        # k = 10
        # 2, 3, 4, 12, 32, 44, 66, 120
        # 2, 1
        
        # 2, 3, 4, 8, 10 => prefixCnt - ((maxi - currElement) * cnt)
        # 4, 1, 0, 4, 6

        # 4, 1, 0, 0, 1, 2, 1, 2

        # 2, 1
        # 8, 7, 6, 2, 0

        # 20-15 = 5, 20-2 = 18

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
                s = s - (maxi - nums[index]) * diff

                if s <= rem:
                    r = mid
                else:
                    l = mid + 1
            
            return l
        
        def bn_r(l, r, index, val, rem):
            while l < r:
                mid = (l + r) // 2
                diff = index - mid
                s = prefix[mid] - prefix[index] + (maxi-nums[mid])
                s = s - (maxi - nums[index]) * diff

                if s >= rem:
                    r = mid
                else:
                    l = mid + 1
            
            return l
        # print(nums)
        for i in range(1, n):
            num = nums[i]

            left = bn_l(0, i, i, num, k)
            s = abs(prefix[i] - prefix[left])
            right = bn_r(i, n-1, i, num, k-s)

            ret = max(ret, right-left+1)
            # print(i, num, (left, right), (right-left))
        
        return ret