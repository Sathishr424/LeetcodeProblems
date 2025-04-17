# Last updated: 17/4/2025, 7:29:13 pm
class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        relation = [0] * n

        for i, num in enumerate(nums2):
            relation[num] = i

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
        
        for i in range(n):
            num = relation[nums1[i]]
            left = query(num)
            right = (n-num-1)-(i-left)
            ret += left * right
            update(num+1)
        
        return ret
        