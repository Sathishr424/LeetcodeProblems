# Last updated: 22/4/2025, 2:11:43 am
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        compression = {}
        index = 1

        arr = []
        for num in nums:
            arr.append(num)
            arr.append(num * 2)
        
        for num in sorted(arr):
            if num not in compression:
                compression[num] = index
                index += 1
        
        n = index + 1
        m = n + 1
        tree = [0] * m

        def add(index):
            while index < m:
                tree[index] += 1
                index += index & -index
        
        def query(index):
            s = 0
            while index:
                s += tree[index]
                index -= index & -index
            return s

        ret = 0
        added = defaultdict(int)
        for num in nums[::-1]:
            ret += query(compression[num]) - added[num]
            
            add(compression[num * 2])
            added[num*2] += 1
        
        return ret