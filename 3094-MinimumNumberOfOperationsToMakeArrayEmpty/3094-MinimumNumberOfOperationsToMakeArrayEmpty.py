# Last updated: 12/6/2025, 5:36:15 am
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        hash = {}
        for num in nums:
            if num in hash: hash[num] += 1
            else: hash[num] = 1
        ret = 0
        for num in hash:
            cnt = hash[num]
            if cnt == 1: return -1
            elif cnt % 3 == 0: ret += cnt // 3
            elif cnt % 3 == 1:
                ret += (cnt-4) // 3 + 2 
            else:
                ret += cnt // 3 + 1
        return ret