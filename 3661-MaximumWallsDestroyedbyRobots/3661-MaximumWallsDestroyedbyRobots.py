# Last updated: 25/8/2025, 3:54:23 pm
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
        
        prefix = [0]
        w = 0
        for i in range(c_index):
            if i in c_walls:
                w += 1
            prefix.append(w)

        left = [0] * n
        right = [0] * n
        between = [0] * n

        def query(l, r):
            return prefix[r + 1] - prefix[l]

        for i in range(n):
            rob, dis = combined[i]
            l = compressed[max(robots[i-1] + 1, rob - dis) if i > 0 else rob - dis]
            left[i] = query(l, compressed[rob])

            r = compressed[min(robots[i+1] - 1, rob + dis) if i + 1 < n else rob + dis]
            right[i] = query(compressed[rob], r)

            if i + 1 < n:
                between[i] = query(compressed[robots[i]], compressed[robots[i + 1]])

        @cache
        def rec(index, is_left):
            if index >= n: return 0

            r, d = combined[index]
            ans = -inf
            
            if is_left:
                ans = left[index] + rec(index + 1, True)
            
            ans = max(ans, right[index] + rec(index + 1, False))
            if index + 1 < n:
                ans = max(ans, min(right[index] + left[index + 1], between[index]) + rec(index + 2, True))
            
            return ans
        
        return rec(0, True)