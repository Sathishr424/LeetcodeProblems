# Last updated: 15/4/2025, 11:47:00 pm
mod = 10**9 + 7
class Solution:
    def createSortedArray(self, ins: List[int]) -> int:
        n = len(ins)
        nums = []

        for i, num in enumerate(ins):
            nums.append((num, i))
        
        nums.sort()
        indexes = {}

        for i in range(n):
            indexes[nums[i][0]] = i

        tree = [0] * (n*4)
        cache = [0] * n

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
        for num in ins:
            i = indexes[num]

            ret = (ret + min(query(0, i-1, 0, n-1, 0), query(i+1, n-1, 0, n-1, 0))) % mod

            index = cache[i]
            tree[index] += 1

            while index > 0:
                index = (index+1) // 2 - 1
                tree[index] = tree[index*2+1] + tree[index*2+2]
        
        return ret