# Last updated: 14/4/2025, 6:13:43 pm
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ret = []
        n = len(nums)
    
        hash = {}
        for num in nums:
            if num in hash: hash[num] += 1
            else: hash[num] = 1
        
        def rec(counter, arr):
            if len(arr) == n: return ret.append(list(arr))
            
            for num in counter:
                if counter[num]:
                    arr.append(num)
                    counter[num] -= 1
                    rec(counter, arr)
                    arr.pop()
                    counter[num] += 1

        rec(hash, [])
        return ret
            