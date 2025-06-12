# Last updated: 12/6/2025, 5:34:38 am
inf = float('inf')
class Solution:
    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:
        hash = defaultdict(lambda: inf)
        ret = []

        maxi = max(groups)

        for i, el in enumerate(elements):
            if el in hash: continue
            hash[el] = i
            
            if el == 1: continue
            
            for j in range(el, maxi+1, el):
                hash[j] = min(hash[j], i)

        ret = []
        for group in groups:
            index = min(hash[group], hash[1])

            ret.append(-1 if index == inf else index)
        
        return ret
        
                    
        
            

            