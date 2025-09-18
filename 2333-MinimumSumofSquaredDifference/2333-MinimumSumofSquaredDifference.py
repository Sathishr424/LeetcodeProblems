# Last updated: 18/9/2025, 10:51:55 am
class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        n = len(nums1)

        diff_arr = []
        for i in range(n):
            diff_arr.append(abs(nums1[i] - nums2[i]))
        
        l = 0
        r = max(diff_arr)

        def isGood(mid):
            need = 0
            for i in range(n):
                need += max(0, diff_arr[i] - mid)

            return need <= (k1 + k2)

        def getRem(mid):
            need = 0
            for i in range(n):
                need += max(0, diff_arr[i] - mid)

            return (k1 + k2) - need
            
        while l < r:
            mid = (l + r) // 2

            if isGood(mid):
                r = mid
            else:
                l = mid + 1

        rem = getRem(l)
        new_diff = []
        for i in range(n):
            new_diff.append(min(diff_arr[i], l))
        
        new_diff.sort(reverse=True)
        ret = 0
        for i in range(n):
            diff = new_diff[i]
            if rem and diff > 0:
                diff -= 1
                rem -= 1
            ret += diff ** 2

        return ret
            