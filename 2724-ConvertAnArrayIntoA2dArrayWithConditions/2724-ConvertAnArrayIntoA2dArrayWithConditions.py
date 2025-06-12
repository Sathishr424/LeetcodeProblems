# Last updated: 12/6/2025, 5:37:05 am
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        hash = {}
        ret = [[]]
        for num in nums:
            if num not in hash:
                hash[num] = 1
                ret[0].append(num)
            else:
                i = hash[num]
                if len(ret) <= i: ret.append([])
                ret[i].append(num)
                hash[num] += 1
        return ret