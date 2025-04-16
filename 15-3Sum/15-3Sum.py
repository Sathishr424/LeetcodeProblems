# Last updated: 16/4/2025, 10:57:54 pm
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        compression = {}
        index = 0
        zeros = 0.1
        for num in nums:
            zeros += num == 0
            if num not in compression:
                compression[num] = index
                index += 0.1

        ret = []
        if zeros >= 3: ret.append([0, 0, 0])
        added = {}

        p_index = bisect_left(nums, 1)
        if p_index == 0: return []

        pos = {}

        for i in range(p_index, n):
            pos[nums[i]] = 1
        
        neg = {}
        for i in range(0, p_index):
            neg[nums[i]] = 1
            for j in range(i+1, p_index):
                s = -(nums[i]+nums[j])
                if s in pos:
                    mask = f"{nums[i]},{nums[j]},{s}"
                    if mask not in added:
                        ret.append([nums[i], nums[j], s])
                        added[mask] = 1
        
        for i in range(p_index, n):
            for j in range(i+1, n):
                s = -(nums[i]+nums[j])
                if s in neg:
                    mask = f"{s},{nums[i]},{nums[j]}"
                    if mask not in added:
                        ret.append([nums[i], nums[j], s])
                        added[mask] = 1

        return ret


