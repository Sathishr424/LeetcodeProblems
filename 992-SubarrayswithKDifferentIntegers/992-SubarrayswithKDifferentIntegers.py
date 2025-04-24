# Last updated: 24/4/2025, 11:18:25 am
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ret = 0

        uniq = [[0, 0] for _ in range(n+1)]
        matches = 0
        left = 0
        prev = 0

        cnt_matches = 0
        cnt_left = 0

        for i in range(n):
            uniq[nums[i]][1] += 1
            cnt_matches += uniq[nums[i]][1] == 1

            if cnt_matches > k:
                while cnt_left < i and cnt_matches > k:
                    num = nums[cnt_left]
                    uniq[num][1] -= 1
                    cnt_matches -= uniq[num][1] == 0
                    cnt_left += 1
                prev = 0
            
            uniq[nums[i]][0] += 1
            matches += uniq[nums[i]][0] == 1

            if matches == k:
                while left <= i and matches == k:
                    num = nums[left]
                    uniq[num][0] -= 1
                    matches -= uniq[num][0] == 0
                    left += 1
                    prev += 1
 
            ret += prev
        
        return ret
        