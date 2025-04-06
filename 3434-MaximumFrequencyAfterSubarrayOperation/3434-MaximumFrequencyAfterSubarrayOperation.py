# Last updated: 6/4/2025, 5:35:03 am
cmin = lambda x, y: x if x < y else y
cmax = lambda x, y: x if x > y else y

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)
        m = 51

        res = 0

        freq = [0] * m
        nums_start = [n] * m
        nums_end = [0] * m
        
        for i in range(n):
            num = nums[i]
        
            nums_start[num] = cmin(i, nums_start[num])
            
            nums_end[num] = i
            
            freq[num] += 1

        for num in range(1, m):
            f = freq[num]
            if f == 0: continue

            start = nums_start[num]
            end = nums_end[num]

            ans = 0
            maxi = ans

            for i in range(start, end+1):
                if nums[i] == k:
                    ans = cmax(ans-1, -1)
                elif nums[i] == num:
                    ans = cmax(ans+1, 1)
                else:
                    ans = cmax(ans, 0)
                
                maxi = cmax(maxi, ans)
        
            res = cmax(res, maxi+freq[k])
        
        return res