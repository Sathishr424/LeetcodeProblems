# Last updated: 21/5/2025, 6:07:18 am
class Solution:
    def numberOfArrays(self, diff: List[int], lower: int, upper: int) -> int:
        ret = 0
        arr = [lower]
        for num in diff:
            arr.append(arr[-1]+num)
        
        mini = min(arr)
        maxi = max(arr)
        maxi += lower-mini
        
        return max(0, upper-maxi+1)