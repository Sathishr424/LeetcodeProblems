# Last updated: 16/4/2025, 2:46:41 am
class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)

        tree = [0] * (n * 4)
        cache = [0] * n

        relation = [0] * n

        for i, num in enumerate(nums2):
            relation[num] = i
        
        arr = []
        for num in nums1:
            arr.append(relation[num])

        def buildTree(left, right, index):
            if left == right:
                cache[left] = index
                return

            mid = (left+right) // 2
            buildTree(left, mid, index*2+1)
            buildTree(mid+1, right, index*2+2)
        
        buildTree(0, n-1, 0)

        def query(l, r, left, right, index):
            if left > r or right < l: return 0

            if left >= l and right <= r: return tree[index]
            mid = (left+right) // 2

            return query(l, r, left, mid, index*2+1) + query(l, r, mid+1, right, index*2+2)
        
        ret = 0

        for num in arr[::-1]:
            right = query(num+1, n-1, 0, n-1, 0)
            left = query(0, num-1, 0, n-1, 0)

            ret += right * (num-left)

            index = cache[num]
            tree[index] = 1

            while index > 0:
                index = (index+1) // 2 - 1
                tree[index] = tree[index*2+1] + tree[index*2+2]

        return ret