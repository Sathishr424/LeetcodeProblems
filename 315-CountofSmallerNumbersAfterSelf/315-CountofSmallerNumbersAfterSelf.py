# Last updated: 15/4/2025, 9:41:06 pm
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        tree = [0] * (n*4)
        ret = [0] * n

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

        for num, i in arr:
            index = 0
            l = 0
            r = n-1

            while l < r:
                mid = (l+r) // 2
                index *= 2
                if i > mid:
                    l = mid+1
                    index += 2
                else:
                    r = mid
                    index += 1
            
            tree[index] = 1

            while index > 0:
                index = (index+1) // 2 - 1
                tree[index] = tree[index*2+1] + tree[index*2+2]
            
            ret[i] = query(i, 0, n-1, 0) - 1
        
        return ret
        