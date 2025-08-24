# Last updated: 25/8/2025, 5:08:21 am
class SegmentTree:
    def __init__(self, n, walls):
        self.n = n
        self.walls = walls
        self.tree = [0] * (self.n * 4)

        self.build(0, self.n-1, 0)
    
    def build(self, l, r, index):
        if l == r:
            self.tree[index] = 1 if l in self.walls else 0
            return self.tree[index]
        
        mid = (l + r) // 2
        left = self.build(l, mid, index * 2 + 1)
        right = self.build(mid + 1, r, index * 2 + 2)

        self.tree[index] = left + right
        return self.tree[index]
    
    def query(self, l, r, index, left, right):
        if l > right or r < left:
            return 0
        
        if l >= left and r <= right:
            return self.tree[index]
        
        mid = (l + r) // 2

        return self.query(l, mid, index * 2 + 1, left, right) + self.query(mid + 1, r, index * 2 + 2, left, right)

class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        n = len(robots)
        combined = []
        for i in range(n):
            combined.append((robots[i], distance[i]))
        
        combined.sort(key=lambda x: x[0])
        robots.sort()

        compressed = {}
        c_index = 0

        total = set(robots + walls)
        for r, c in combined:
            total.add(r - c)
            total.add(r + c)
            total.add(r - 1)
            total.add(r + 1)

        for x in sorted(total):
            if x not in compressed:
                compressed[x] = c_index
                c_index += 1
            
        c_walls = {}
        for wall in walls:
            c_walls[compressed[wall]] = 1
        
        tree = SegmentTree(c_index, c_walls)

        left = [0] * n
        right = [0] * n

        for i in range(n):
            rob, dis = combined[i]
            l = compressed[max(robots[i-1] + 1, rob - dis) if i > 0 else rob - dis]
            left[i] = tree.query(0, c_index-1, 0, l, compressed[rob])

            r = compressed[min(robots[i+1] - 1, rob + dis) if i + 1 < n else rob + dis]
            right[i] = tree.query(0, c_index-1, 0, compressed[rob], r)


        @cache
        def rec(index, is_left):
            if index >= n: return 0

            r, d = combined[index]
            ans = -inf
            
            if is_left:
                ans = left[index] + rec(index + 1, True)
            
            ans = max(ans, right[index] + rec(index + 1, False))
            if index + 1 < n:
                between = tree.query(0, c_index-1, 0, compressed[robots[index]], compressed[robots[index + 1]])
                ans = max(ans, min(right[index] + left[index + 1], between) + rec(index + 2, True))
            
            return ans
        
        return rec(0, True)