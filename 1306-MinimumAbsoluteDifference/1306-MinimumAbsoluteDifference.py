# Last updated: 12/6/2025, 5:42:58 am
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        diff = float('inf')
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] <= diff:
                if arr[i] - arr[i-1] == diff:
                    ret.append([arr[i-1], arr[i]])
                else: 
                    ret = [[arr[i-1], arr[i]]]
                    diff = arr[i] - arr[i-1]
        return ret