# Last updated: 12/6/2025, 5:39:04 am
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        there = defaultdict(int)
        for st in arr:
            there[st] += 1
        
        for i in range(len(arr)):
            if there[arr[i]] == 1:
                k -= 1
                if k == 0: return arr[i]
        
        return ''