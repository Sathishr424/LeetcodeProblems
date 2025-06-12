# Last updated: 12/6/2025, 5:35:43 am
class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        indexes = []
        for i in range(n):
            match = True
            if i-1 >= 0:
                match = match and nums[i] % 2 != nums[i-1] % 2
            if i+1 < n:
                match = match and nums[i] % 2 != nums[i+1] % 2
            
            if not match: indexes.append(i)
        
        ret = []
        for x, y in queries:
            if x-y == 0:
                ret.append(True)
                continue
            l = 0
            r = len(indexes)-1
            if x+1 < n and nums[x] % 2 == nums[x+1] % 2:
                ret.append(False)
                continue
            if y-1 >= 0 and nums[y] % 2 == nums[y-1] % 2:
                ret.append(False)
                continue
            
            x += 1
            y -= 1
            match = True
            while l <= r:
                mid = (l+r)//2
                if indexes[mid] < x:
                    l = mid+1
                elif indexes[mid] > y:
                    r = mid-1
                else:
                    match = False
                    break
            ret.append(match)
        
        return ret



