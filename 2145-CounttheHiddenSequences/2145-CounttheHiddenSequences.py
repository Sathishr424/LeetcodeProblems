# Last updated: 21/5/2025, 6:04:38 am
class Solution:
    def numberOfArrays(self, diff: List[int], lower: int, upper: int) -> int:
        ret = 0
        arr = [lower]
        for num in diff:
            arr.append(arr[-1]+num)
        
        mini = min(arr)
        maxi = max(arr)
        diff = lower-mini
        maxi += diff
        
        return max(0, upper-maxi+1)