# Last updated: 12/6/2025, 5:38:26 am
class Solution:
    def countRectangles(self, rect: List[List[int]], points: List[List[int]]) -> List[int]:
        n = len(rect)
        rect.sort(key=lambda x: (x[0], x[1]))

        tree = [SortedList() for _ in range(n*4)]

        def build(index, left, right):
            if left == right:
                tree[index].add(rect[left][1])
                return tree[index]
            
            mid = (left+right) // 2
            left = build(index*2+1, left, mid)
            right = build(index*2+2, mid+1, right)
            
            tree[index].update(left)
            tree[index].update(right)
            return tree[index]
        
        def query(i, j, index, left, right, y):
            if right < i or left > j: return 0
            
            if left >= i and right <= j: return bn_right(tree[index], y)

            mid = (left+right) // 2
            
            return query(i, j, index*2+1, left, mid, y) + query(i, j, index*2+2, mid+1, right, y)

        build(0, 0, n-1)

        def bn_left(val):
            l = 0
            r = n
            while l < r:
                mid = (l+r) // 2
                if rect[mid][0] >= val: r = mid
                else: l = mid+1 
            return l

        def bn_right(arr, val):
            l = 0
            r = len(arr)
            while l < r:
                mid = (l+r) // 2
                if arr[mid] >= val: r = mid
                else: l = mid+1 
            return len(arr) - l
        
        ret = []

        for x, y in points:
            ret.append(query(bn_left(x), n-1, 0, 0, n-1, y))

        return ret