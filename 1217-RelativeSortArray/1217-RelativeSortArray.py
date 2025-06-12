# Last updated: 12/6/2025, 5:43:36 am
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        h1 = {}
        
        for num in arr2:
            h1[num] = 1
        
        h2 = defaultdict(int)
        last = []
        ret = []

        for num in arr1:
            if num in h1: h2[num] += 1
            else: last.append(num)
        
        for num in arr2:
            for _ in range(h2[num]):
                ret.append(num)
        
        return ret + sorted(last)
