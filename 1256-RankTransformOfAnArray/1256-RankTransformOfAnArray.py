# Last updated: 12/6/2025, 5:43:23 am
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        hash = {}
        rank = 1
        for num in sorted(arr):
            if num not in hash: 
                hash[num] = rank
                rank += 1
        
        for i in range(len(arr)):
            arr[i] = hash[arr[i]]
        
        return arr