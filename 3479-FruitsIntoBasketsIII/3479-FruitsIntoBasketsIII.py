# Last updated: 6/6/2025, 7:37:44 pm
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)

        tree = [0 for _ in range(n*4)]

        def query(l, r, index, need):
            if tree[index] < need: return False
            
            if l == r:
                tree[index] = 0
                return True

            mid = (l + r) // 2

            left = query(l, mid, index*2+1, need)
            right = False
            if not left:
                right = query(mid+1, r, index*2+2, need)
            
            tree[index] = max(tree[index*2+1], tree[index*2+2])
            return left or right

        def build(l, r, index):
            if l == r:
                tree[index] = baskets[l]
                return tree[index]
            mid = (l+r) // 2
            left = build(l, mid, index*2+1)
            right = build(mid+1, r, index*2+2)

            tree[index] = max(left, right)
            return tree[index]
        
        build(0, n-1, 0)

        ret = 0
        for i in range(n):
            ret += not query(0, n-1, 0, fruits[i])

        return ret