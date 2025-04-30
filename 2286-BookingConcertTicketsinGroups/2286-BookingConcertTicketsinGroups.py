# Last updated: 30/4/2025, 8:26:10 am
class Node:
    def __init__(self, maxSeats=0, totalSeats=0):
        self.totalSeats = totalSeats
        self.maxSeats = maxSeats

class BookMyShow:
    def __init__(self, n: int, m: int):
        """
        [5, 5, 5, 5, 5]

        (4, 1)
        """
        self.n = n
        self.m = m

        self.tree = [Node(m) for _ in range(n*4)]
        self.cache = [0] * n

        def buildTree(l, r, index):
            if l == r:
                self.cache[l] = index
                self.tree[index].totalSeats = m
                return self.tree[index]
            
            mid = (l+r) // 2

            left = buildTree(l, mid, index*2+1)
            right = buildTree(mid+1, r, index*2+2)

            self.tree[index].totalSeats = left.totalSeats + right.totalSeats

            return self.tree[index]
        
        buildTree(0, n-1, 0)
    
    def scatter_query(self, l, r, maxRow, index, s):
        if s == 0 or l > maxRow or self.tree[index].totalSeats == 0:
            return s

        if l == r:
            available = min(s, self.tree[index].totalSeats)
            self.tree[index].totalSeats -= available
            self.tree[index].maxSeats -= available
            return s - available

        mid = (l + r) // 2
        left = index * 2 + 1
        right = index * 2 + 2

        s = self.scatter_query(l, mid, maxRow, left, s)
        s = self.scatter_query(mid + 1, r, maxRow, right, s)

        self.tree[index].totalSeats = self.tree[left].totalSeats + self.tree[right].totalSeats
        self.tree[index].maxSeats = max(self.tree[left].maxSeats, self.tree[right].maxSeats)

        return s
    
    def queryRange(self, l, r, start, end, index):
        if l > end or r < start: return 0

        mid = (l+r) // 2

        if l >= start and r <= end:
            return self.tree[index].totalSeats
        return self.queryRange(l, mid, start, end, index*2+1) + self.queryRange(mid+1, r, start, end, index*2+2)
    
    def query(self, l, r, start, end, index, s):
        if self.tree[index].maxSeats < s or l > end: return self.n

        if l == r: return l

        mid = (l+r) // 2

        ans = self.query(l, mid, start, end, index*2+1, s)
        if ans == self.n:
            return self.query(mid+1, r, start, end, index*2+2, s)
        
        return ans

    def gather(self, k: int, maxRow: int) -> List[int]:
        index = self.query(0, self.n-1, 0, maxRow, 0, k)

        if index < self.n:
            ret = [index, self.m - self.tree[self.cache[index]].maxSeats]
            self.tree[self.cache[index]].maxSeats -= k
            self.tree[self.cache[index]].totalSeats -= k

            index = self.cache[index]

            while index:
                index = (index - 1) // 2
                left = index*2+1
                right = index*2+2
                self.tree[index].totalSeats = self.tree[left].totalSeats + self.tree[right].totalSeats
                self.tree[index].maxSeats = max(self.tree[left].maxSeats, self.tree[right].maxSeats)
            
            return ret
        return []

    def scatter(self, k: int, maxRow: int) -> bool:
        if self.queryRange(0, self.n-1, 0, maxRow, 0) < k: return False
        return self.scatter_query(0, self.n-1, maxRow, 0, k) == 0


# Your BookMyShow object will be instantiated and called as such:
# obj = BookMyShow(n, m)
# param_1 = obj.gather(k,maxRow)
# param_2 = obj.scatter(k,maxRow)