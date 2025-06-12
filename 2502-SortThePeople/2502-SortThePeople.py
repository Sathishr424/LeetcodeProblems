# Last updated: 12/6/2025, 5:37:50 am
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        arr = []
        for i in range(len(names)):
            arr.append((i, heights[i]))
        
        arr.sort(key=lambda x: -x[1])

        return [names[a[0]] for a in arr]