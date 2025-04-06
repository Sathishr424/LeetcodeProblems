# Last updated: 6/4/2025, 5:32:33 am
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)

        res = 0
        freq = [0] * 51

        nums_start = {}
        nums_end = {}
        
        for i in range(n):
            num = nums[i]
        
            if num not in nums_start:
                nums_start[num] = i
            
            nums_end[num] = i
            
            freq[num] += 1

        for num in nums_start:
            f = freq[num]

            start = nums_start[num]
            end = nums_end[num]

            ans = 0
            maxi = ans

            for i in range(start, end+1):
                if nums[i] == k:
                    ans = max(ans-1, -1)
                elif nums[i] == num:
                    ans = max(ans+1, 1)
                else:
                    ans = max(ans, 0)
                
                maxi = max(maxi, ans)
        
            res = max(res, maxi+freq[k])
        
        return res