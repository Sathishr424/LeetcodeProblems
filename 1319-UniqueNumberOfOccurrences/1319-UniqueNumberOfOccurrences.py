# Last updated: 12/6/2025, 5:42:55 am
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hash = {}
        for num in arr:
            if num in hash: hash[num] += 1
            else: hash[num] = 1
        second_hash = {}
        for num in hash:
            if hash[num] in second_hash: return False
            second_hash[hash[num]] = 1
        return True