# Last updated: 4/7/2025, 2:17:28 am
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        n = len(nums)

        freq = [0] * (n + 1)
        ret = 0
        prev = 0
        cnt = 0
        prev_2 = 0

        for i in range(n):
            freq[nums[i]] += 1
            if freq[nums[i]] == 1:
                cnt += 1

                if cnt > k:
                    prev = prev_2
                    while cnt > k:
                        freq[nums[prev]] -= 1
                        if freq[nums[prev]] == 0: cnt -= 1
                        prev += 1
                    
                    prev_2 = prev
            if cnt == k:
                while freq[nums[prev_2]] > 1:
                    freq[nums[prev_2]] -= 1
                    prev_2 += 1

                ret += prev_2 - prev + 1
        
        return ret