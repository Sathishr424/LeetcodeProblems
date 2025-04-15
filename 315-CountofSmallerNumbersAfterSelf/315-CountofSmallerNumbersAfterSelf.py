# Last updated: 15/4/2025, 10:07:40 pm
class Solution:
    def countSmaller(self, nums):
        # Step 1: Coordinate compression
        sorted_unique = sorted(set(nums))
        rank = {val: idx for idx, val in enumerate(sorted_unique)}
        n = len(rank)

        # Segment tree
        tree = [0] * (n * 4)

        def update(index, left, right, pos):
            if left == right:
                tree[index] += 1
                return
            mid = (left + right) // 2
            if pos <= mid:
                update(index*2+1, left, mid, pos)
            else:
                update(index*2+2, mid+1, right, pos)
            tree[index] = tree[index*2+1] + tree[index*2+2]

        def query(index, left, right, ql, qr):
            if qr < left or ql > right:
                return 0
            if ql <= left and right <= qr:
                return tree[index]
            mid = (left + right) // 2
            return query(index*2+1, left, mid, ql, qr) + query(index*2+2, mid+1, right, ql, qr)

        res = []
        for num in reversed(nums):
            r = rank[num]
            count = query(0, 0, n-1, 0, r-1)  # Count smaller elements
            res.append(count)
            update(0, 0, n-1, r)

        return res[::-1]
