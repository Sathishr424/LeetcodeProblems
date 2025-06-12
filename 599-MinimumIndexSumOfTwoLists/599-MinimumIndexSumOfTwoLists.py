# Last updated: 12/6/2025, 5:48:10 am
class Solution:
    def findRestaurant(self, l1: List[str], l2: List[str]) -> List[str]:
        hash = {}

        for i, w in enumerate(l1):
            if w not in hash:
                hash[w] = i

        least = len(l1)+len(l2)
        tmp = defaultdict(list)

        for i, w in enumerate(l2):
            if w in hash:
                if i+hash[w] <= least:
                    tmp[i+hash[w]].append(w)
                    least = i+hash[w]
        
        return tmp[least]
