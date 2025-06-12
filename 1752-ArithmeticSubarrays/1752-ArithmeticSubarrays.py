# Last updated: 12/6/2025, 5:40:38 am
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        n = len(l)

        for i in range(n):
            arr = []
            for j in range(l[i], r[i]+1):
                arr.append(nums[j])
            arr.sort()
            k = 2
            tmp = arr[1] - arr[0]
            while k < len(arr) and arr[k] - arr[k-1] == tmp:
                k += 1
            
            ans.append(k == len(arr))
        return ans
            
                