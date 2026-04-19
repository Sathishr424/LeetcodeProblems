# Last updated: 4/19/2026, 7:58:10 AM
1class Solution:
2    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
3        m = len(nums1)
4        n = len(nums2)
5
6        rev_arr = nums1[::-1]
7        ans = 0
8
9        for i in range(n-1, -1, -1):
10            index = bisect_right(rev_arr, nums2[i]) - 1
11            if rev_arr[index] <= nums2[i]:
12                index = m - index - 1
13                ans = max(ans, i - index)
14                # print(i, nums2[i], index, ans)
15        
16        return ans
17
18