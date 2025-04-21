# Last updated: 22/4/2025, 2:24:38 am
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
        added = 0
        for num in nums:
            ret += added - query(compression[num * 2])
            
            add(compression[num])
            added  += 1
        
        return ret