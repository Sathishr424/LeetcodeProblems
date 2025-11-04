# Last updated: 4/11/2025, 9:09:20 am
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        ret = []
        for i in range(n-k+1):
            freq = defaultdict(int)
            for j in range(i, i+k):
                freq[nums[j]] += 1
            arr = []
            for num in freq:
                arr.append((freq[num], num))
            arr.sort(reverse=True)
            tot = 0
            for j in range(min(x, len(arr))):
                tot += arr[j][1] * arr[j][0]
            ret.append(tot)
        
        return ret