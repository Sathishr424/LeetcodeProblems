# Last updated: 12/6/2025, 5:42:09 am
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        hash = {}
        for num in arr:
            if num*2 in hash or (num % 2 == 0 and num//2 in hash): return True
            hash[num] = 1
        return False