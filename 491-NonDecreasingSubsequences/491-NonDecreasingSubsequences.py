# Last updated: 12/6/2025, 5:49:01 am
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = set()

        for n in nums[::-1]:
            new = set()

            for cur in res:
                if n <= cur[0]:
                    new.add((n,)+cur)
            
            res.update(new)
            res.add((n,))

        return list(filter(lambda x: len(x)>1,map(lambda x: list(x), res)))