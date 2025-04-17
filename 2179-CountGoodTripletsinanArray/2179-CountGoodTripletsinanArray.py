# Last updated: 17/4/2025, 7:27:23 pm
class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        relation = [0] * n

        for i, num in enumerate(nums2):
            relation[num] = i
        
        arr = []
        for num in nums1:
            arr.append(relation[num])

        m = n+1
        tree = [0] * (m+1)
        ret = 0

        def query(index):
            s = 0
            while index:
                s += tree[index]
                index -= index & -index
            return s
        
        def update(index):
            while index <= m:
                tree[index] += 1
                index += index & -index
        
        for i, num in enumerate(arr):
            left = query(num)
            right = (n-num-1)-(i-left)
            ret += left * right
            update(num+1)
        
        return ret
        