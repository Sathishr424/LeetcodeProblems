# Last updated: 6/4/2025, 9:32:13 am
class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        cnt = 0
        while True:
            match = True
            for i in range(1, len(nums)):
                if nums[i] < nums[i-1]: 
                    match = False
            if match: return cnt
            sums = []
            for i in range(len(nums)-1):
                arr = nums[:i+1] + nums[i+2:]
                arr[i] += nums[i+1]
                sums.append([nums[i] + nums[i+1], arr])
            
            sums.sort(key = lambda x: x[0])
            nums = sums[0][1]
            cnt += 1

        return 0
        