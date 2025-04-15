# Last updated: 15/4/2025, 10:12:24 pm
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        tree = [0] * (n*4)
        ret = [0] * n
        cache = [-1] * n

        def buildTree(left, right, index):
            if left == right:
                cache[left] = index
                return

            mid = (left+right) // 2
            buildTree(left, mid, index*2+1)
            buildTree(mid+1, right, index*2+2)
        
        buildTree(0, n-1, 0)

        def query(l, left, right, index):
            if right < l: return 0

            if left >= l and right < n:
                return tree[index]

            mid = (left+right) // 2

            return query(l, left, mid, index*2+1) + query(l, mid+1, right, index*2+2)

        arr = []

        for i, num in enumerate(nums):
            arr.append((num, i))
        
        arr.sort()

        for j in range(n-1):
            i = arr[j][1]
            ret[i] = query(i+1, 0, n-1, 0)

            index = cache[i]
            tree[index] = 1

            while index > 0:
                index = (index+1) // 2 - 1
                tree[index] = tree[index*2+1] + tree[index*2+2]
        
        ret[arr[n-1][1]] = query(arr[n-1][1]+1, 0, n-1, 0)
        return ret
        