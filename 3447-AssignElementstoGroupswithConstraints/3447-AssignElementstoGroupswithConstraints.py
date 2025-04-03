# Last updated: 3/4/2025, 4:07:54 pm
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
        
                    
        
            

            