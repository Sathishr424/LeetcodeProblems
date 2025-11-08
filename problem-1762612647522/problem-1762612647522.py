# Last updated: 8/11/2025, 8:07:27 pm
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        ans = 0
        for i in range(n):
            cnt = 0
            for j in range(i, n):
                if nums[j] == target:
                    cnt += 1
                window = j - i + 1
                if cnt > window // 2:
                    ans += 1

        return ans