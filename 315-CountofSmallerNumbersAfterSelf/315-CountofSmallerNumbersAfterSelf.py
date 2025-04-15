# Last updated: 15/4/2025, 11:20:33 pm
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ret = [0] * n

        freq = {}
        index = 0

        for num in sorted(nums):
            if num not in freq:
                freq[num] = index
                index += 1
        
        n = len(freq)

        tree = [0] * (n*4)
        cache = [-1] * n

        def buildTree(left, right, index):
            if left == right:
                cache[left] = index
                return

            mid = (left+right) // 2
            buildTree(left, mid, index*2+1)
            buildTree(mid+1, right, index*2+2)
        
        buildTree(0, n-1, 0)

        def query(r, left, right, index):
            if left > r: return 0

            if right <= r:
                return tree[index]

            mid = (left+right) // 2

            return query(r, left, mid, index*2+1) + query(r, mid+1, right, index*2+2)

        for j in range(len(nums)-1, -1, -1):
            num = nums[j]
            i = freq[num]

            ret[j] = query(i-1, 0, n-1, 0)

            index = cache[i]
            tree[index] += 1

            while index > 0:
                index = (index+1) // 2 - 1
                tree[index] = tree[index*2+1] + tree[index*2+2]
            
        return ret
        