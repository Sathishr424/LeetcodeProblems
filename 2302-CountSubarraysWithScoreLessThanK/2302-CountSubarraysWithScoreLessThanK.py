# Last updated: 28/4/2025, 4:42:00 pm
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        """
        [2,1,4,3,5]
        """
        ret = 0
        prefix = [0]

        for num in nums:
            prefix.append(prefix[-1] + num)
        
        n = len(nums)

        for i in range(n):
            l = 0
            r = i+1

            while l < r:
                mid = (l+r) // 2

                cnt = i-mid+1
                s = prefix[i+1] - prefix[mid]

                if s*cnt < k:
                    r = mid
                else:
                    l = mid+1

            ret += i-l+1

        return ret
                    

