# Last updated: 1/8/2026, 10:49:19 AM
1class Solution:
2    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
3        m = len(nums1)
4        n = len(nums2)
5
6        @cache
7        def rec(i, j, used):
8            if i == m or j == n: 
9                return 0 if used else -inf
10
11            ans = max(rec(i + 1, j, used), rec(i, j+1, used))
12            ans = max(ans, rec(i+1, j+1, 1) + nums1[i] * nums2[j])
13
14            return ans
15        
16        ans = rec(0, 0, 0)
17        rec.cache_clear()
18        return ans