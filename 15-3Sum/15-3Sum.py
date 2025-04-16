# Last updated: 17/4/2025, 12:29:54 am
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        n = len(nums)
        ret = []

        compression = {}
        index = 0
        for num in nums:
            if num not in compression:
                compression[num] = index
                index += 1

        added = {}
        for i in range(n):
            for j in range(i+1, n):
                s = target - (nums[i]+nums[j])
                sums = {}
                for k in range(j+1, n):
                    diff = s-nums[k]
                    if diff in sums:
                        mask = hash((compression[nums[i]], compression[nums[j]], compression[diff], compression[nums[k]]))
                        if mask not in added:
                            ret.append([nums[i], nums[j], diff, nums[k]])
                            added[mask] = 1
                    sums[nums[k]] = 1
        
        return ret


