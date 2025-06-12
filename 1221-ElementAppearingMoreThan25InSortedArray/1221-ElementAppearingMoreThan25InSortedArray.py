# Last updated: 12/6/2025, 5:43:32 am
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        off = int((n * 0.25) + 1)
        prev = None
        cnt = 0
        for num in arr:
            if num == prev:
                cnt += 1
                if cnt == off: return num
            else:
                cnt = 1
                prev = num
        return arr[0]