# Last updated: 12/6/2025, 5:40:58 am
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ret = 0
        l = 1
        while l <= len(arr):
            for i in range(len(arr)):
                #print(arr[i:i+l])
                if l <= len(arr[i:]):
                    for j in arr[i:i+l]: ret += j
            l+=2
        return ret