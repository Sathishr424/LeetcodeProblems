# Last updated: 3/22/2026, 2:21:23 PM
1from typing import List
2
3class Solution:
4    def uniformArray(self, nums1: list[int]) -> bool:
5        n = len(nums1)
6        odd = False
7        even = False
8        for num in nums1:
9            if num % 2:
10                odd = True
11            else:
12                even = True
13
14        # for odd
15        for i in range(n):
16            if nums1[i] % 2 == 0:
17                if not odd: break
18        else:
19            return True
20        
21        for i in range(n):
22            if nums1[i] % 2:
23                if not even: break
24        else:
25            return True
26
27        return False