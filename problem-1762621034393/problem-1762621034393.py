# Last updated: 8/11/2025, 10:27:14 pm
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        ones = 0
        sl = SortedList()
        sl.add(0)
        ans = 0
        for i in range(n-1, -1, -1):
            if nums[i] == target:
                ones += 1
            else:
                ones -= 1

            ans += sl.bisect_left(ones)
            sl.add(ones)

        return ans
                
        