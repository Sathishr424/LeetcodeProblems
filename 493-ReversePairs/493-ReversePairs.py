# Last updated: 22/4/2025, 2:10:46 am
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
        
        # -4, -3, -2, -1, 0, 1, 2, 3, 4

        ret = 0
        added = defaultdict(int)
        for num in nums[::-1]:
            x = query(compression[num]) - added[num]
            ret += x
            
            add(compression[num * 2])
            added[num*2] += 1
        
        return ret