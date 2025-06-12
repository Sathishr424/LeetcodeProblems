# Last updated: 12/6/2025, 5:55:13 am
relation = ['', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if n == 0: return []

        nums = []
        for d in digits:
            nums.append(relation[int(d)-1])
        
        ret = []

        def rec(i, st):
            if i == n: return ret.append(st)

            for j in range(len(nums[i])):
                rec(i+1, st+nums[i][j])
        
        rec(0, '')
        return ret

        


