# Last updated: 4/7/2025, 2:07:44 am
class Solution:
    def countAtMostK(self, arr, k):
        n = len(arr)
        
        freq = defaultdict(int)
        cnt = 0
        prev = 0
        ret = 0
        
        for i in range(n):
            freq[arr[i]] += 1
            if freq[arr[i]] == 1:
                cnt += 1
            
                while cnt > k:
                    freq[arr[prev]] -= 1
                    if freq[arr[prev]] == 0:
                        cnt -= 1
                    prev += 1
            
            ret += i - prev + 1
        
        return ret
    
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        x = self.countAtMostK(nums, k)
        y = self.countAtMostK(nums, k - 1)
        return x - y