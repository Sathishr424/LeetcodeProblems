# Last updated: 12/25/2025, 7:09:03 PM
class PSegmentTree:
    def __init__(self, n, nums, compressed):
        self.n = n
        self.roots = []
        self.lefts = []
        self.rights = []
        self.sums = []
        self.cnts = []
        self.node_index = 0
        self.roots.append(self.build(0, n-1))
        for i, num in enumerate(nums):
            self.roots.append(self.update(self.roots[-1], 0, self.n-1, compressed[(num, i)], num))

    def getNewNode(self, l=-1, r=-1, cnt=0, sum=0):
        if l != -1 and r != -1:
            cnt = self.cnts[l] + self.cnts[r]
            sum = self.sums[l] + self.sums[r]
        self.cnts.append(cnt)
        self.sums.append(sum)
        self.lefts.append(l)
        self.rights.append(r)
        self.node_index += 1
        return self.node_index - 1
    
    def build(self, l, r):
        if l == r: return self.getNewNode()
        mid = (l + r) // 2

        return self.getNewNode(self.build(l, mid), self.build(mid + 1, r))

    def update(self, node, l, r, pos, sum):
        if l == r:
            return self.getNewNode(cnt=self.cnts[node] + 1, sum=self.sums[node] + sum)
        
        mid = (l + r) // 2

        if pos <= mid:
            return self.getNewNode(self.update(self.lefts[node], l, mid, pos, sum), self.rights[node])
        return self.getNewNode(self.lefts[node], self.update(self.rights[node], mid + 1, r, pos, sum))
    
    def _getKthSmallest(self, left, right, l, r, k):
        if l == r:
            return l
        
        mid = (l + r) // 2
        left_count = self.cnts[self.lefts[right]]- self.cnts[self.lefts[left]]
        if left_count >= k:
            return self._getKthSmallest(self.lefts[left], self.lefts[right], l, mid, k)
        return self._getKthSmallest(self.rights[left], self.rights[right], mid + 1, r, k - left_count)
    
    def _getFirstKSum(self, left, right, l, r, k):
        if l == r:
            return self.sums[right] - self.sums[left]
        
        mid = (l + r) // 2
        left_count = self.cnts[self.lefts[right]]- self.cnts[self.lefts[left]]
        if left_count >= k:
            return self._getFirstKSum(self.lefts[left], self.lefts[right], l, mid, k)
        return (self.sums[self.lefts[right]] - self.sums[self.lefts[left]]) + self._getFirstKSum(self.rights[left], self.rights[right], mid + 1, r, k - left_count)

    def getKthSmallest(self, l, r, k):
        return self._getKthSmallest(self.roots[l], self.roots[r+1], 0, self.n-1, k)
    
    def getFirstKSum(self, l, r, k):
        return self._getFirstKSum(self.roots[l], self.roots[r+1], 0, self.n-1, k)

class Solution:
    def minOperations(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        divided = []
        prefix = [0]
        new_nums = []
        for i, num in enumerate(nums):
            divided.append(num // k)
            prefix.append(prefix[-1] + divided[-1])
            new_nums.append((divided[-1], i))
        compressed = {}
        uncompressed = [0] * n
        new_nums.sort()
        index = 0
        for num, i in new_nums:
            compressed[(num, i)] = index
            uncompressed[index] = num
            index += 1
        
        same_group = [0] * n
        i = 0
        group = 0
        while i < n:
            rem = nums[i] % k
            while i < n and nums[i] % k == rem:
                same_group[i] = group
                i += 1
            group += 1

        segTree = PSegmentTree(index, divided, compressed)
        ret = []
        for l, r in queries:
            if same_group[l] != same_group[r]:
                ret.append(-1)
                continue
            
            window = r - l + 1
            half = window // 2
            if window % 2:
                med = segTree.getKthSmallest(l, r, half + 1)
                median = uncompressed[med]
                leftSum = segTree.getFirstKSum(l, r, half + 1)
                remSum = (prefix[r + 1] - prefix[l]) - leftSum
                ret.append((median * (half + 1) - leftSum) + (remSum - median * half))
            else:
                median_l = uncompressed[segTree.getKthSmallest(l, r, half)]
                median_r = uncompressed[segTree.getKthSmallest(l, r, half + 1)]
                median = (median_l + median_r) // 2
                leftSum = segTree.getFirstKSum(l, r, half)
                remSum = (prefix[r + 1] - prefix[l]) - leftSum
                ret.append((median * half - leftSum) + (remSum - median * half))
        
        return ret